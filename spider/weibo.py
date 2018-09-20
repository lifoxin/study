#!/usr/bin/env python3

import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient

'''
爬取马云的微博，打开F12,Network，All,getIndex。。查看Headers 和 Previes
Headers主要看下面的参数和Preview的json数据,注意在Header中的base_url和Referer，下面就是整理数据的过程。
这个实例演示 Ajax 的模拟请求过程，爬取的结果不是重点，主要是为了学会怎样去分析 Ajax 请求，怎样用程序来模拟抓取 Ajax 请求，了解了相关抓取原理！
另外学会使用MongoDB操作！
'''

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2145291155',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
client = MongoClient()    #创建MongoDB对象
db = client['weibo']
collection = db['weibo']
max_page = 10


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2145291155',
        'containerid': '1076032145291155',
        'page': page
    }
    url = base_url + urlencode(params) 
 #调用了 urlencode() 方法将参数转化为 URL 的 GET请求参数，即类似于type=uid&value=2145291155&containerid=1076032145291155&page=2 ,形成一个新的 URL
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json(),page   #调用 json() 方法将内容解析为 Json 返回
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json,page:int):                      #调入两个参数
    if json:
        items = json.get('data').get('cards')        #获取json中，data之下的cards的字典
        for index,item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
                item = item.get('mblog')            #在item中获取mblog的键值
                weibo = {}                          #创建新字典
                weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()  #转化成文本格式
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                yield weibo                         #生成器返回一个yield


def save_to_mongo(result):
    if collection.insert(result):                    #插入数据库MongoDB
        print('Saved to Mongo')                      #打印出结果


if __name__ == '__main__':
    for page in range(1, max_page + 1):
        json = get_page(page)
        results = parse_page(*json)   #调用元组参数
        for result in results:
            print(result)
            save_to_mongo(result)
