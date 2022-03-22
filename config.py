# 配置爬虫需要的各个参数
class SpiderConfig(object):
    cookie = "Cookie: _Collect_UD=cSR6_Fb3MdUMGR4_kXCww; _Collect_UD_Create_Time=Sat%20Mar%2005%202022%2009%3A57%3A46%20GMT+0800%20%28%u4E2D%u56FD%u6807%u51C6%u65F6%u95F4%29; _ga=GA1.2.1529785872.1646445467; gr_user_id=91a0c606-a444-42da-9781-cc3bdd54a57d; searchType=pub; Hm_lvt_dc703135c31ddfba7bcda2d15caab04e=1646445467,1646728512,1647759938; Hm_lvt_789fd650fa0be6a2a064d019d890b87f=1646445467,1646728512,1647759938; _Collect_ISNEW=1647759938132; _YS_userAccect=NJq9YbYI-SyuJHL5ylnSy; _gid=GA1.2.1253943599.1647948880; aminer_access_token=%22eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI3MThkOTg3Zi00NGI1LTQzM2ItOGRiNi1lMmVjYWY5Y2VmMjYiLCJpZCI6IjYyMjYwNjYwNmVlZWFlYTI1OGIwMDA0YSIsImNpZCI6ImEyMjcyOTljLTBmYTQtNGNiZS05NWE4LWE4YWY3Y2U0ODM3YyIsInQiOiJQYXNzd29yZCJ9.8EcS5Qw88hNHZJ2dCru9F9KR4dwIM7sNhDTq_o4jkR4%22; aminer_refresh_token=%22b6258521-dfd4-4c59-9ed8-ea34a84e0235%22; _Collect_SN=83; Hm_lpvt_dc703135c31ddfba7bcda2d15caab04e=1647951773; Hm_lpvt_789fd650fa0be6a2a064d019d890b87f=1647951773; gr_session_id_ae8dfb99e5e4cda1=b0f73695-ce22-42de-9270-80a91fc568c2; _gat_gtag_UA_1156684_2=1; gr_session_id_ae8dfb99e5e4cda1_b0f73695-ce22-42de-9270-80a91fc568c2=true"
    # 一般情况下的hearders
    normal_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30',
                      'Cookie':cookie}
    # 用于搜索的headers,需要带Host等参数
    search_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30',
                      'Content-Type': 'application/json;charset=UTF-8;application/json;charset=UTF-8;',
                      'Sec-Fetch-Site': 'same-site',
                      'Host': 'searchtest.aminer.cn',
                      'Origin': 'https://www.aminer.cn',
                      'Referer': 'https://www.aminer.cn/',
                      'Connection': 'keep-alive',
                      'Cookie':cookie}
    # 关键词搜索api
    search_url = "https://searchtest.aminer.cn/aminer-search/search/publication"
    # 最新会议资讯api,须填入page
    confir_infor_url = 'https://www.aminer.cn/research_report/articlelist?classify=%E4%BC%9A%E8%AE%AE%E8%AE%BA%E6%96%87&page={}'
    # 论文主页链接,须填入论文id
    paper_url = "https://www.aminer.cn/pub/{}"
    # 资讯文章url, 须填入文章id
    infor_url = "https://www.aminer.cn/research_report/{}?download=false&classify=%E4%BC%9A%E8%AE%AE%E8%AE%BA%E6%96%87"
    # 会议论文
    confer_url = 'https://dblp.org/db/conf/{0}/{0}2021.html'
    # acl会议论文
    acl_url = "https://aclanthology.org/events/acl-2021/"
    # 热门主题url
    hottopic_url = 'https://apiv2.aminer.cn/magic?a=__domains.GetTopicOfDomain___'
    # 热门主题请求数据
    hottopic_postdata = [{"action":"domains.GetTopicOfDomain","parameters":{"topicSize":20,"topSize":50,"sids":[143]}}]
    # 获取bib信息api
    cite_url = "https://apiv2.aminer.cn/magic?a=getTopicCited__topic.GetTopicCited___"
    # 获取reference信息api
    ref_url = "https://api.aminer.cn/api/pub/ref/{}/offset/0/size/30"
                