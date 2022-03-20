
# 配置爬虫需要的各个参数
class SpiderConfig(object):
    # 一般情况下的hearders
    normal_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30'}
    # 用于搜索的headers,需要带Host等参数
    search_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30',
                      'Content-Type': 'application/json;charset=UTF-8;application/json;charset=UTF-8;',
                      'Sec-Fetch-Site': 'same-site',
                      'Host': 'searchtest.aminer.cn',
                      'Origin': 'https://www.aminer.cn',
                      'Referer': 'https://www.aminer.cn/',
                      'Connection': 'keep-alive'}
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
                