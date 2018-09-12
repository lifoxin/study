#!/usr/bin/env python3

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["rookie"]
mycol = mydb["site2"]

mylist = [
    {"_id":1,"name":"shanghai","color":"red"},
    {"_id":2,"name":"beijing","color":"white"},
    {"_id":3,"name":"guangzhou","color":"black"},
    {"_id":4,"name":"shenzhen","color":"green"},
    {"_id":5,"name":"hangzhou","color":"yellow"}
]

x = mycol.insert_many(mylist)

print(x.inserted_ids)
