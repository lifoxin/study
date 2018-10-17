#!/usr/bin/env python3

import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from config import *
from urllib.parse import quote

# browser = webdriver.Chrome()

MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'

KEYWORD = 'meizu'

MAX_PAGE = 10

SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
#browser = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(browser, 10)
#client = pymongo.MongoClient(MONGO_URL)
#db = client[MONGO_DB]

def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        print("browser.get(url)")
        if page > 1:
            print("page > 1")
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
            print("submit.click()")
        print("wait.until")
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        print("下一步get_products()")
        get_products()
        print("get_products()")
    except TimeoutException:
        print("超时，20秒等待")
        index_page(page)
        
def get_products():
    """
    提取商品数据
    """
    print("get_products,提取商品数据")
    html = browser.page_source
    doc = pq(html)
    print("doc")
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        print("for item in items")
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        print("save_to_monogo(product)")
        save_to_mongo(product)
        print("保存到mongo数据库")
def save_to_mongo(result):
    """
    保存至MongoDB
    :param result: 结果
    """
    print("写入mongo的记录中")
    client = pymongo.MongoClient(MONGO_URL)
    db = client[MONGO_DB]
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')

def main():
    """
    遍历每一页
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
    browser.close()

if __name__ == '__main__':
    main()
