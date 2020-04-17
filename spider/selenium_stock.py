#!/usr/bin/env python3

from selenium.webdriver import PhantomJS
import json

'''
使用selenium工具爬取股票的最新情况，保存为jl格式
通过by_class_name和by_tag_name获取节点，数据是表格格式，用for循环遍历
使用dict((zip())) 把不同类型组合成字典，最后写入js,打印出来
'''
if __name__=='__main__':
    url = "http://data.10jqka.com.cn/ipo/xgsgyzq/"
    ofile = open('stock.jl','w')

    d = PhantomJS()
    d.get(url)
    header = ['股票代码','股票简称','申购代码','发行价格']
    for tr in d.find_elements_by_class_name('m_tbd'):
        for td in tr.find_elements_by_tag_name('tr'):
            values = [text.text for text in td.find_elements_by_tag_name('td')]
            if not values:
                continue
            values = values[:3] + [float(x) if x.isdigit() else -1 for x in values[7]]
            record = dict(zip(header,values))
            ofile.write(json.dumps(record) + '\n')
            ofile.flush()
            print(record)
    ofile.close()
    d.quit()


