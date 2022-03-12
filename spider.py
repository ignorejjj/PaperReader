import requests 
from bs4 import BeautifulSoup
import json

# 获取热门会议论文资讯
# 原始网址:https://www.aminer.cn/research_report/articlelist?classify=%E4%BC%9A%E8%AE%AE%E8%AE%BA%E6%96%87&page=2
# 返回值为list,包含论文资讯的标题、作者、摘要、时间、文章链接、图片链接
# [{paper1},{paper2},...]
def get_confir_infor(page_num = 1):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30'}
    paper_data = []
    for page in range(1,page_num+1):
        url = 'https://www.aminer.cn/research_report/articlelist?classify=%E4%BC%9A%E8%AE%AE%E8%AE%BA%E6%96%87&page={}'.format(page)
        data = requests.get(url, headers = headers).text.split("window.g_initialProps =")[1]
        data = json.loads(data.split(";")[0])['report']['reportList']
        for item in data:
            paper_url = "https://www.aminer.cn/research_report/{}?download=false&classify=%E4%BC%9A%E8%AE%AE%E8%AE%BA%E6%96%87".format(item['_id'])
            img_url = item['image']
            abstract = item['abstract']
            title = item['title']
            author = item['author']
            time = item['update_time'][:10]
            paper_data = paper_data.append({"title":title, "author":author, "abstract":abstract, "time":time, "img_url":img_url, "paper_url":paper_url})
    return paper_data


# 根据填入关键词，返回搜索结果
# 返回值为list,包含论文的名称，pdf链接，作者，详细页面的url，摘要，期刊名
# [{paper1},{paper2},...]
def search_paper(keyword):
    headers = {'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30',
               'Content-Type': 'application/json;charset=UTF-8;application/json;charset=UTF-8;',
               'Sec-Fetch-Site': 'same-site',
               'Host': 'searchtest.aminer.cn',
               'Origin': 'https://www.aminer.cn',
               'Referer': 'https://www.aminer.cn/',
               'Connection': 'keep-alive'}
    url = "https://searchtest.aminer.cn/aminer-search/search/publication"
    post_data = {"query":"{}".format(keyword),"needDetails":True,"page":2,"size":20,"aggregations":[{"field":"keywords.keyword","size":20,"type":"terms"},{"field":"authors.orgid","size":20,"type":"terms"},{"field":"year","size":100,"type":"terms"}],"filters":[{"boolOperator":0,"type":"term","value":"143","field":"domains"}]}
    result = json.loads(requests.post(url, headers = headers, data = json.dumps(post_data)).text)
    search_data = []
    for item in result['data']['hitList']:
        title = item['title']
        pdf_url = item['pdf']
        author = [j['name'] for j in item['authors']]
        paper_url = "https://www.aminer.cn/pub/{}".format(item['id'])
        abstract = item['pubAbstract']
        journal_name = item['venue']['raw']
        search_data.append({"title":title, "pdf_url":pdf_url, "author":author, "paper_url":paper_url, "abstract":abstract, "journal_name":journal_name})
    return search_data

# 获取会议论文
# 会议包括: ICCV,CVPR,SIGIR,NIPS,ICML,AAAI,IJCAI,MM,KDD,CIKMD等
# 返回值为dict,包含所查询会议的所有论文的名称以及种类(Long) 
# {"part1":[paper1,paper2,...],"part2":[paper3,paper4]}
def get_conference_paper():
    # iclr,cvpr,cikm,icml,kdd,mm,cikm,sigir
    # aaai,iccv 需要修改一下part_name(后续进行添加)
    # acl 需要对另一个api进行爬取
    url = 'https://dblp.org/db/conf/aaai/aaai2021.html'
    req = requests.get(url).text
    soup =BeautifulSoup(req,"lxml")
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
        return output
    
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
        return output