import os

import requests

requestHead = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}


# 下载图片
def load_down_picture(url, targetPath, **kwargs):
    response = requests.get(url, headers=requestHead)
    alias = None
    if 'alias' in kwargs:
        alias = kwargs['alias']

    if not os.path.exists(targetPath):
        os.makedirs(targetPath)
    content = response.content
    subffix = url[url.rindex('.'):]

    # 如果未要求别名
    if alias is None or alias.strip() == '':
        picNmae = url[url.rindex('/'):]
    else:
        picNmae = alias + subffix

    picFile = open(targetPath + '/' + picNmae, 'wb')
    picFile.write(content)
    picFile.close()


if __name__ == '__main__':
    url = 'https://pic3.zhimg.com/80/v2-4c4ff7eaf60f811375a02e1e91f49dae_hd.jpg'
    load_down_picture(url, '/Users/yangzhi/Desktop/projects/python/spider/pictures')
    pass
