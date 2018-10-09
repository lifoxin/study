#!/usr/bin/env python3

from lxml import etree
import requests
import json

def getTree(url):
    r = requests.get(url)
    if r.status_code == 200:
        r.encoding = r.apparent_encoding
        html = r.text
        tree = etree.HTML(html)
    else:
        print("r.status_code != 200")
    return tree

def fetch(tree):
    content = tree.xpath('//span[@class="bjh-p"]//text()')
    for text in content:
        print(text+'\n')

def store(text):
    with open('text','w') as f:
        data = json.dumps(text,ensure_ascii=False)
        f.write(data + '\n\n')
        f.close()

if __name__=='__main__':

    url = 'https://baijiahao.baidu.com/s?id=1604042409489140786&wfr=spider&for=pc'
    tree = getTree(url)
    fetch(tree)
