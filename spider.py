import requests 
from bs4 import BeautifulSoup
import json
import os
from config import SpiderConfig
from utils import *

class Spider():
    def __init__(self):
        # 热门资讯
        self.infor_data = []
        # 会议论文
        self.confer_data = []
        # 热门主题
        self.hottopics = []
    
    # 根据填入关键词，返回搜索结果
    # 返回值:[{paper1},{paper2},...],包含论文的名称，pdf链接，作者，详细页面的url，摘要，期刊名
    def search_paper(self, keyword):
        post_data = {"query":keyword,
                     "needDetails":True,
                     "page":0,
                     "size":20,
                     "aggregations":[{"field":"keywords.keyword","size":20,"type":"terms"},{"field":"authors.orgid","size":20,"type":"terms"},{"field":"year","size":100,"type":"terms"}],
                     "filters":[{"boolOperator":0,"type":"term","value":"143","field":"domains"}]}
        req = requests.post(SpiderConfig.search_url,
                            headers = SpiderConfig.search_headers, 
                            data = json.dumps(post_data))
        result = json.loads(req.text)
        search_data = []
        # 解析网页,获取论文各项信息
        for item in result['data']['hitList']:
            title = item['title']
            pdf_url = item['pdf']
            author = [j['name'] for j in item['authors']]
            # 论文主页链接
            paper_url = SpiderConfig.paper_url.format(item['id'])
            abstract = item['pubAbstract']
            journal_name = item['venue']['raw']
            search_data.append({"title":title, "pdf_url":pdf_url, "author":author, "paper_url":paper_url, "abstract":abstract, "journal_name":journal_name})
        return search_data
    
    # 获取热门会议论文资讯
    # page_num: 需要获取的页数
    # 返回值: [{paper1},{paper2},...],包含论文资讯的标题、作者、摘要、时间、文章链接、图片链接
    def get_confir_infor(self, page_num = 1):
        infor_data = []
        for page in range(1,page_num+1):
            url = SpiderConfig.confir_infor_url.format(page)
            data = requests.get(url, headers = SpiderConfig.normal_headers).text
            data = data.split("window.g_initialProps =")[1]
            data = json.loads(data.split(";")[0])['report']['reportList']
            for item in data:
                # 资讯文章url
                paper_url = SpiderConfig.infor_url.format(item['_id'])
                # 封面图片url
                img_url = item['image']
                abstract = item['abstract']
                title = item['title']
                author = item['author']
                time = item['update_time'][:10]
                infor_data = infor_data.append({"title":title, "author":author, "abstract":abstract, "time":time, "img_url":img_url, "paper_url":paper_url})
        self.infor_data = infor_data
        return infor_data

    # 获取最近一年顶会论文,包括: ICCV,CVPR,ACL等
    # 返回值: {"part1":[paper1,paper2,...],"part2":[paper3,paper4]}
    # confer_name: iclr,cvpr,cikm,icml,kdd,mm,cikm,sigir,acl
    def get_conference_paper(self, confer_name):
        # acl需要对另一个api进行爬取
        if confer_name == "acl":
            output = self.get_acl_paper()
            self.confer_data["acl"] = output
            return output
        
        url = SpiderConfig.confer_url.format(confer_name)
        req = requests.get(url, headers = SpiderConfig.normal_headers)
        soup =BeautifulSoup(req.text, "lxml")
        
        # 首先获取会议各个部分的名称
        part_name = []
        for item in soup.find("div",{"id":"main"}).find_all("header"):
            part = item.find("h2")
            if part:
                part_name.append(part.text)

        # 针对icml,neurips等没有子模块的会议进行处理
        if part_name == []:
            output = {}
            temp = []
            result = soup.find("ul",{"class":"publ-list"}).find_all("li")[1:]
            for item in result:
                paper = item.find("span",{"class":"title"})
                if paper:
                    temp.append(paper.text)
            output['no-name'] = temp
        else: 
            # 第一个项为会议名称,删去
            part_name = part_name[1:]
            # 获取每个部分下的论文名称
            result = soup.find_all("ul",{"class":"publ-list"})[1:]
            output = {}
            for ind,item in enumerate(result):
                temp = []
                res = item.find_all("li")
                for i in res:
                    paper = i.find("span",{"class":"title"})
                    if paper:
                        temp.append(paper.text)
                output[part_name[ind]] = temp
        self.confer_data[confer_name] = output
        return output
    
    # 获取acl会议文章
    # 返回值为list: [paper1,paper2,...]
    def get_acl_paper(self):
        req = requests.get(SpiderConfig.acl_url, headers = SpiderConfig.normal_headers)
        soup =BeautifulSoup(req.text, "lxml")
        res = soup.find_all("strong")[1:]
        output = [item.text for item in res]
        return output 
    
    # 热门主题爬取
    # 返回值: [hottopic1,hottopic2,...] 
    def get_hottopic(self):
        req = requests.post(SpiderConfig.hottopic_url, 
                                       headers=SpiderConfig.search_headers,
                                       data=json.dumps(SpiderConfig.hottopic_postdata))
        req = json.loads(req.text)
        result = req['data'][0]['data']['hotTopics']
        hottopics = [item['name'] for item in result]
        self.hottopics = hottopics
        return hottopics
    
    # 搜索给定文献的所有参考文献,并保存为bib文件
    # 返回值: [ref_name1,ref_name2,..]
    def get_ref(self, paper_name):
        # 获取给定文献的主页url
        res = self.search_paper(paper_name)
        paper_url = res[0]['paper_url']

        # 访问paper_url,获取该文献的所有参考文献
        req = requests.get(paper_url, headers = SpiderConfig.normal_headers)
        soup =BeautifulSoup(req.text, 'lxml')
        result = soup.find_all("li",{"class":"refItem"})
        res = [item.text for item in result]
        filepath = ".\Reference{}".format(paper_name)
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        ref_names = []
        # 对每个参考文献,保存该文献的bib
        for i,ref_name in enumerate(resetscreen):
            outname = self.get_bib(ref_name, filepath)
            if outname != "NotFound" or outname!= "None":
                ref_names.append(outname)
        return ref_names 
    

    # 获取某个文献的bib文件(get_ref的子函数)
    # ref_name:文献名称, filepath:保存路径
    def get_bib(self, ref_name, filepath):
        # 由于ref_ame中包含了作者，出版刊物等无用信息，需要进行简化再搜索
        paper_name = simplify_name(ref_name)
        # 说明该文献为网址等形式,无法搜索,跳过
        if paper_name is None:
            print("None", ref_name)
            return "None"
        res = self.search_paper(paper_name)
        # aminer无收录该文章
        # ---后续需要对这部分进行改进(添加搜索源)---
        if res == []:
            print("NotFound:", paper_name)
            return "NotFound"

        paper_id = res[0]['paper_url'].split("/")[-1]   
        post_data = [{"action":"topic.GetTopicCited", "parameters":{"ids":[paper_id]}}]
        req = requests.post(SpiderConfig.cite_url, data=json.dumps(post_data))
        req = json.loads(req.text)
        ref = req['data'][0]['data']['bib']
        with open(filepath + "\\" + "{}.bib".format(paper_name),"w",encoding='utf-8') as f:
            f.write(ref)
        return paper_name