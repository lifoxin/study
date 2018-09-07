#!/usr/bin/env python3


from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

'''
 robotparser 模块的基本用法和实例讲解，利用它我们就可以方便地判断哪些页面可以抓取
'''


rp = RobotFileParser()
rp.parse(urlopen('https://www.baidu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('*', '://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_8580596602608074179%22%7D&n_type=0&p_from=1'))
print(rp.can_fetch('*', "https://www.baidu.com/search?q=python&page=1&type=collections"))
