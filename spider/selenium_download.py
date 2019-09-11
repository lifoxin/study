from selenium import webdriver
from lxml import etree
import os
import requests

def get_html(url):
    d = webdriver.Chrome()
    try:
        d.get(url)
        d.implicitly_wait(5)
        return d.page_source
    finally:
        d.quit()

def parse_html(html):
    html = etree.HTML(html)
    imgurls = []
    li_tags = html.xpath("//ol[@class='commentlist']/li[@id]")
    for li_tag in li_tags:
        imgurl = 'http://' + li_tag.xpath(".//div[@class='text']//img/@src")[0].replace("//","")
        print(imgurl)
        imgurls.append(imgurl)
    return imgurls

def download_img(url,num):
    if 'img' in os.listdir(r'C:\Users\Administrator\Desktop\image'):
        pass
    else:
        os.mkdir(r'C:\Users\Administrator\Desktop\image\img')
    os.chdir(r'C:\Users\Administrator\Desktop\image\img')
    imag = requests.get(url).content
    suffix = url.split('.')[-1]
    with open(str(num) + '.' + suffix,'wb') as f:
        print('正在下载：%s' %url)
        f.write(imag)

if __name__ == '__main__':
    url = 'http://jandan.net/ooxx'
    html = get_html(url)
    imgurls = parse_html(html)
    for i in range(len(imgurls)):
        download_img(imgurls[i],i)

