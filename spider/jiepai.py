#!/usr/bin/env python3

import requests
from urllib.parse import urlencode
from requests import codes
import os
from hashlib import md5
from multiprocessing.pool import Pool

'''
街拍，希望你能读懂。
使用多进程池pool爬取数据，由页面滚动,发现ajax请求的后续链接的参数offset在变化，所以只要传offset参数就可以构成新url。

'''
def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    base_url = 'https://www.toutiao.com/search_content/?'
    url = base_url + urlencode(params)
    try:
        resp = requests.get(url)
        if codes.ok == resp.status_code:
            return resp.json()              #如果返回状态码为 200,调用 response 的 json() 方法将结果转为 Json 格式
    except requests.ConnectionError:
        return None


def get_images(json):              #爬取Ajax请求的数据，有JS生成
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {
                    'image': 'https:' + image.get('url'),
                    'title': title
                }


def save_image(item):
    img_path = 'img' + os.path.sep + item.get('title')   #构造存放图片的路径
    if not os.path.exists(img_path):
        os.makedirs(img_path)                            #如果不存在路径，就新建
    try:
        resp = requests.get(item.get('image'))           #通过图片的链接，生成图片
        if codes.ok == resp.status_code:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                    file_name=md5(resp.content).hexdigest(),file_suffix='jpg')    #构造生成图片的目录路径
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)                                        #将爬取的图片以二进制保存到目录路径
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image，item %s' % item)


def main(offset):            #调用参数，爬取内容，保存内容
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


GROUP_START = 0
GROUP_END = 7

if __name__ == '__main__':
    pool = Pool()            #创建进程池
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)   #用了多线程的线程池，调用其 map() 方法实现多线程下载。
    pool.close()
    pool.join()
