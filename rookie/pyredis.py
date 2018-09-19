#!/usr/bin/env python3

#官方推荐使用StrictRedis类的相关方法
from redis import StrictRedis

#声明一个StrictRedis对象
redis = StrictRedis(host='localhost',port=6379,db=0,password='')
#调用set()方法，设置一个键值对
redis.set('name','Bob')
#获取打印
print(redis.get('name'))

#redis的方法太多了。先去了解如何使用，再熟悉连接Python的方法
