#!/usr/bin/env python3

import requests
from lxml import etree
import json
from threading import Thread
import queue
'''
爬取前程无忧网站的运维岗位，通过搜索相关字，在这一页中，爬取多个公司相同岗位的重要信息。
使用xpath的提取工具，构造二级页面进行爬取，把信息保存为字典，再转化json格式写入文件。
代码相对不难，不写注释。
'''
class QianChenSpider(Thread):
   
    def __init__(self,url,q):
        super(QianChenSpider,self).__init__()
        self.url = url
        self.q = q
   
    def run(self):      #获取当前页的url,爬取数据
        urls = self.geturl(self.url)
        for url in urls:
            if not self.parse_page(url):
                continue
            self.parse_page(url)

    def geturl(self,url):  #获取当前网页的其他招聘url
        r = requests.get(url)
        if r.status_code == 200:
            html = r.text
            tree = etree.HTML(html)
            urls = tree.xpath('//div[@class="el"]/p[1]/span/a/@href')
        else:
            print("r.status_code != 200")
        return urls

    def parse_page(self,url):  #根据招聘网页的详细信息，整理成一个字典
        r = requests.get(url)
        if r.ok:
            try:
                r.encoding = r.apparent_encoding
                html = r.text
                tree = etree.HTML(html)
                company = tree.xpath('//p[@class="cname"]//@title')
                money = tree.xpath('//div[@class="cn"]//strong/text()')
                title = tree.xpath('//div[@class="cn"]/h1/@title')
                require = tree.xpath('//div[@class="bmsg job_msg inbox"]/p/text()')
                addr = tree.xpath('/html/body/div[3]/div[2]/div[3]/div[2]/div/p/text()')
                if len(addr) >= 2:
                    addr = addr[1].strip()
                if len(company) >= 1:
                    company = company[0].strip()
                if len(money) >= 1:
                    money = money[0].strip()
                if len(title) >= 1:
                    title = title[0].strip()
                my_dict = {'title':title,'company':company,'money':money,'require':require,'addr':addr}
                print(my_dict)
            except:
                print("url:%s爬虫失败"%url)

def nexturl(url):  #获取网页的下一页url
    r = requests.get(url)
    if r.status_code == 200:
        html = r.text
        tree = etree.HTML(html)
        nexturl = tree.xpath('//div[@class="p_in"]//@href')
    else:
        print("r.status_code != 200")
    return nexturl

def main():
    #创建一个队列用来保存进程获取到的数据
    q = queue.Queue()
    #保存线程
    Thread_list = []
    base_url = "https://search.51job.com/list/040000,040300,0000,00,9,99,%25E8%25BF%2590%25E7%25BB%25B4%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=17&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    urls = nexturl(base_url) + [base_url]
    #创建并启动线程
    for url in urls:
        p = QianChenSpider(url,q)
        p.start()
      #  print("开启线程%d"%count)
        Thread_list.append(p)
    
    #让主线程等待子线程执行完成
    for i in Thread_list:
        if not i.join():
            continue
        try:
            i.join()
        except:
            print("%s子进程失败"%i)
    print("it's over")

if __name__ == '__main__':
    main()
