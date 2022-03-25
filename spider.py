"""
Crawler program
"""

import requests 
from bs4 import BeautifulSoup
import json
import os
import re
from config import SpiderConfig
from utils import *
from retrying import retry
from freeproxy import freeproxy

class Spider():
    def __init__(self):
        # proxy ip 
        self.client = freeproxy.FreeProxy(proxy_sources = ['proxylistplus', 'kuaidaili'])
    
    # Search corresponding papers according to keywords
    def search_paper(self, keyword):
        """
        Args:
            keyword: Search content
        
        Output:
            A list containing information for each paper, including title, author, abstract and so on.
            e.g. [{"title":..,"author":...}, {"title":..,"author":...},...]
        """

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
        # Analyze the data to obtain the information of the paper
        for item in result['data']['hitList']:
            title = item['title']
            pdf_url = item['pdf']
            author = [j['name'] for j in item['authors']]
            paper_url = SpiderConfig.paper_url.format(item['id'])
            paper_id = item['id']
            abstract = item['pubAbstract']
            journal_name = item['venue']['raw']
            search_data.append({"title":title, "pdf_url":pdf_url, "author":author, "paper_url":paper_url, "abstract":abstract, "journal_name":journal_name, "paper_id":paper_id})
        return search_data
    
    
    # Search all references of the given literature and save the bib file
    def get_ref(self, paper_name):
        """
        Args:
            paper_name: The name of the paper for which you need to download references
        
        Output:
            [ref_name1,ref_name2,..
        """

        # Get the ID of the document
        res = self.search_paper(paper_name)
        paper_id = res[0]['paper_id']
        name = res[0]['title']
        # Obtain all references of this document
        req = requests.get(SpiderConfig.ref_url.format(paper_id), headers = SpiderConfig.normal_headers)
        data = json.loads(req.text)
        ref_infor = [(item['id'],item['title']) for item in data['data']]
        filepath = ".\Reference data\{}".format(simplify(name))
        if not os.path.exists(filepath):
            os.makedirs(filepath)

        # For each reference, save the bib file of the reference
        print("-------开始下载参考文献bib文件-------")
        for (ref_id, ref_name) in ref_infor:
            print("正在下载bib : "+ref_name)
            self.get_bib(ref_name,ref_id, filepath)
        
        # Return reference names
        ref_names = [item[1] for item in ref_infor]
        return ref_names 
    

    # Get the bib of file of the paper 
    @retry(stop_max_attempt_number=2, wait_fixed=2000)
    def get_bib(self, ref_name,ref_id, filepath): 
        """
        Args:
            ref_name: The name of the paper that needs to download the bib file
            ref_id: The id of the paper that needs to download the bib file
            filepath: Download path
        Output:
            There is no output in this function.
        """
        post_data = [{"action":"topic.GetTopicCited", "parameters":{"ids":[ref_id]}}]
        req = self.client.post(SpiderConfig.cite_url, data=json.dumps(post_data))
        req = json.loads(req.text)
        ref = req['data'][0]['data']['bib']
        ref_name = simplify(ref_name)
        with open(filepath + "\\" + "{}.bib".format(ref_name),"w",encoding='utf-8') as f:
            f.write(ref)
        return None