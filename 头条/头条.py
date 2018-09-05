# -*- coding:utf-8 -*-

import os
import re
import json
import requests

from hashlib import md5
from urllib.parse import urlencode
from requests import RequestException


def get_page_index(offset):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': '迪丽热巴壁纸',
        'armload': 'true',
        'count': 20,
        'cur_tab': 3,
        'from': 'gallery'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        Headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)'
        }
        request = requests.get(url, headers=Headers)
        if request.status_code == 200:
            return request.text
        return None
    except RequestException:
        print('请求出错')
        return None


# 请求关键字索引页

def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


# 将索引页中的目录解析出

def get_page_detail(url):
    try:
        Headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)'
        }
        request = requests.get(url, headers=Headers)
        if request.status_code == 200:
            return request.text
        return None
    except RequestException:
        print('请求详情出错', url)
        return None


# 请求目录页

def parse_page_detail(html, url):
    images_pattern = re.compile(r'"url":"\\/\\/(.*?)",.*?","', re.S)
    result = re.findall(images_pattern, html)
    for i in range(len(result)):
        result[i] = result[i].replace('\\', '')
    return result


def parse_images(url):
    try:
        Headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)'
        }
        request = requests.get(url, headers=Headers)
        if request.status_code == 200:
            return request.content
        return None
    except RequestException:
        print('请求详情出错', url)
        return None


def save_images(content):
    path = '{0}/{1}.{2}'.format(r'D:\迪丽热巴图片', md5(content).hexdigest(), 'jpg')
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(content)


def main(offset):
    html = get_page_index(offset)  # 请求关键字索引页
    for url in parse_page_index(html):  # 将索引页中的目录解析出
        print('正在下载', url)
        html = get_page_detail(url)  # 请求目录页
        if html:
            for result in parse_page_detail(html, url):
                url = 'http://' + result
                html = parse_images(url)
                save_images(html)


if __name__ == '__main__':
    for i in range(0, 400, 20):
        main(i)
