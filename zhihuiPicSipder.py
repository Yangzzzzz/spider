import json

import requests
from lxml import etree

from util import SpiderUtil

url = 'https://www.zhihu.com/api/v4/questions/297715922/answers?' \
      'include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_' \
      'info%2Cis_collapsed%2Cannotation_action%2' \
      'Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%' \
      '2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_' \
      'content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_' \
      'time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion' \
      '%2Cexcerpt%2Crelationship.is_authorized%2Cis_author' \
      '%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis' \
      '_recognized%2Cpaid_info%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D' \
      '.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics' \
      '&limit={}&offset={}&platform=desktop&sort_by=default'
limit = 20
offset = 1
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}


def parseContent(content):
    html = etree.HTML(content)
    figures = html.xpath('//figure/noscript/img/@src')
    for figure in figures:
        SpiderUtil.load_down_picture(figure, '/Users/yangzhi/Desktop/projects/python/spider/pictures')


if __name__ == '__main__':
    realUrl = url.format(limit, offset)
    response = requests.get(realUrl, headers=headers)
    reJson = json.loads(response.text)
    datas = reJson['data']
    for dat in datas:
        parseContent(dat['content'])
