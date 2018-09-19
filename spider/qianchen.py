#!/usr/bin/env python3

import requests
from lxml import etree
import json

'''
爬取前程无忧网站的运维岗位，通过搜索相关字，在这一页中，爬取多个公司相同岗位的重要信息。
使用xpath的提取工具，构造二级页面进行爬取，把信息保存为字典，再转化json格式写入文件。
代码相对不难，不写注释。
'''
def geturl(url):
    r = requests.get(url)
    if r.status_code == 200:
        html = r.text
        tree = etree.HTML(html)
        urls = tree.xpath('//div[@class="el"]/p[1]/span/a/@href')
    else:
        print("r.status_code != 200")
    return urls

def fetch(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    html = r.text
    tree = etree.HTML(html)
    company = tree.xpath('//p[@class="cname"]//@title')
    money = tree.xpath('//div[@class="cn"]//strong/text()')
    title = tree.xpath('//div[@class="cn"]/h1/@title')
    require = tree.xpath('//div[@class="bmsg job_msg inbox"]/p/text()')
    addr = tree.xpath('//div[@class="bmsg inbox"]/p[@class="fp"]/text()')[1].strip()
    my_dict = {'title':title,'company':company,'money':money,'require':require,'addr':addr}
    return my_dict

def store(data):
    with open('job.json','a') as f:
        data = json.dumps(data,ensure_ascii=False)
        f.write(data + '\n\n')
        f.close()

if __name__ == '__main__':
    url = "https://search.51job.com/list/040000,000000,0000,00,9,99,%25E8%25BF%2590%25E7%25BB%25B4%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    urls = geturl(url)
    count = 1
    for url in urls:
        my_dict = fetch(url)
        store(my_dict)
        print("爬取完第%d个job"%count)
        count += 1
    print("一共爬取了%d个网页"%count)
