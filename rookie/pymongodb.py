#!/usr/bin/env python3

import pymongo
#使用pymongo.MongoClient对象连接数据库
myclient = pymongo.MongoClient("mongodb://localhost:27017")
#创建数据库
mydb = myclient["rookie"]
#创建集合（数据表）
mycol = mydb["site2"]
#准备字典类型的列表内容
mylist = [
    {"_id":1,"name":"shanghai","color":"red"},
    {"_id":2,"name":"beijing","color":"white"},
    {"_id":3,"name":"guangzhou","color":"black"},
    {"_id":4,"name":"shenzhen","color":"green"},
    {"_id":5,"name":"hangzhou","color":"yellow"}
]
#插入数据
#x = mycol.insert_many(mylist)

#判断数据库存在
#dblist = myclient.database_names()
#if "rookie" in dblist:
#      print("rookie数据库已存在！")
#
##判断集合存在
#collist = mydb.collection_names()
#if "site2" in collist:   
#      print("site2集合已存在！")

#查找一条数据
#x = mycol.find_one()
#print(x)

##查找所有数据
#for x in mycol.find():
#    print(x)

#查找前3条数据
#for x in mycol.find().limit(3):
#    print(x)

##查询没有_id的字段,有id和name字段的内容
#for x in mycol.find({},{"_id":0,"id":1,"name":1}):
#    print(x)

#查找有name,shanghai的字段
#myquery = {"name":"shanghai"}

#查找name中第一个字母大于等于"h"的数据
#myquery = {"name":{"$gt":"h"}}

#查找name中第一个字母为"s"的数据
#myquery = {"name":{"$regex":"^s"}}

#for x in mycol.find(myquery):
#    print(x)

#update_one()和update_many()可以修改字段，第一个参数是匹配的条件,第二天参数是修改的字段
#newvalues = {"$set":{"color":"blue"}}
#mycol.update_many(myquery,newvalues)
#for x in mycol.find():
#    print(x)

#删除多个文档，delete_many(),第一个参数为查询对象，指定的删除对象
#myquery = {"name":{"$regex":"^h"}}
#mycol.delete_many(myquery)
#mycol.delete_many({})  #删除所有文档，就是集合的数据
#mycol.drop()  #删除集合，就是数据表
#for x in mycol.find():
#    print(x)

#查找排序，sort(),第一个参数是排序的字段，默认1升序，-1降序
#mydoc = mycol.find().sort("id",-1)
#for x in mydoc:
#    print(x)



