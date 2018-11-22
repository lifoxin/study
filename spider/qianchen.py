#!/usr/bin/env python3

import requests
from lxml import etree
import json

'''
爬取前程无忧网站的运维岗位，通过搜索相关字，在这一页中，爬取多个公司相同岗位的重要信息。
使用xpath的提取工具，构造二级页面进行爬取，把信息保存为字典，再转化json格式写入文件。
'''
def geturl(url):  #获取当前网页的其他招聘url
    r = requests.get(url)
    if r.status_code == 200:
        html = r.text
        tree = etree.HTML(html)
        urls = tree.xpath('//div[@class="el"]/p[1]/span/a/@href')
    else:
        print("r.status_code != 200")
    return urls

def nexturl(url):  #获取网页的下一页url
    r = requests.get(url)
    if r.status_code == 200:
        html = r.text
        tree = etree.HTML(html)
        nexturl = tree.xpath('//div[@class="p_in"]//@href')
    else:
        print("r.status_code != 200")
    return nexturl

def fetch(url):  #根据招聘网页的详细信息，整理成一个字典
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    html = r.text
    tree = etree.HTML(html)
    company = tree.xpath('//p[@class="cname"]//@title')
    money = tree.xpath('//div[@class="cn"]//strong/text()')
    title = tree.xpath('//div[@class="cn"]/h1/@title')
    require = tree.xpath('//div[@class="bmsg job_msg inbox"]/p/text()')
    addr = tree.xpath('/html/body/div[3]/div[2]/div[3]/div[2]/div/p/text()') # 因为有的招聘的地址列表没有第二项，所有就全选了
    if len(addr) >= 2:
        addr = addr[1].strip()
    if len(company) >= 1:
        company = company[0].strip()
    if len(money) >= 1:
        money = money[0].strip()
    if len(title) >= 1:
        title = title[0].strip()
    my_dict = {'title':title,'company':company,'money':money,'require':require,'addr':addr}
    return my_dict

def store(data):  #把收集好的字典以json的格式添加到文件中
    with open('job.json','a') as f:
        data = json.dumps(data,ensure_ascii=False)
        f.write(data + '\n\n')
        f.close()

if __name__ == '__main__':
    base_url = "https://search.51job.com/list/040000,000000,0000,00,9,99,%25E8%25BF%2590%25E7%25BB%25B4%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=h"
    count = 1
    urls = geturl(base_url)
    for url in urls:
        my_dict = fetch(url)
        store(my_dict)
        print("爬取完第%d个job"%count)
        count += 1
    print("下一页开始爬取\n")
    for nexturl in nexturl(base_url):    #获取下一页url
        urls = geturl(nexturl)           #当前页其他招聘url
        for url in urls:
            my_dict = fetch(url)
            store(my_dict)
            print("爬取完第%d个job"%count)
            count += 1
        print("下一页开始爬取\n")
    print("一共爬取了%d个网页"%count)
