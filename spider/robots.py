#!/usr/bin/env python3


from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

'''
 robotparser 模块的基本用法和实例讲解，利用它我们就可以方便地判断哪些页面可以抓取
 本人很奇怪，为什么两个都false
'''
#网站可爬取robots协议
roboturl='http://www.jianshu.com/robots.txt'
#测试该网站是否可爬取
url='http://www.jianshu.com/p/b67554025d7d'

rp = RobotFileParser()
rp.set_url(roboturl)
rp.read()
print(rp.can_fetch('*', url))
print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))
