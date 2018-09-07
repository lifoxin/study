#!/usr/bin/env python3

import mysql.connector

#mydb = mysql.connector.connect(     #连接数据库
#        host='localhost',
#        user="felix",
#        passwd="1"
#)

#mycursor = mydb.cursor()  #创建游标

#mycursor.execute("create database rookie")  #执行游标sql语句

#mycursor.execute("show databases")
#for i in mycursor:
#    print(i)


mydb = mysql.connector.connect(     #连接数据库
        host='localhost',
        user="felix",
        passwd="1",
        database="rookie",
)   
mycursor = mydb.cursor()  #创建游标
#mycursor.execute("create table sites (name varchar(255),url varchar(255))")  #创建rookie数据库的数据表 sites

#mycursor.execute("alter table sites add column id int auto_increment primary key ")
# 修改表的列，添加主键

#sql = "insert into sites (name,url) values (%s,%s)"
#val = ("runnoob","https://www.runoob.com")
#val = [
#    ('google','https://www.google.com'),
#    ('github','https://www.github.com'),
#    ('taobao','https://www.taobao.com')
#        ]
#mycursor.executemany(sql,val)
#mycursor.execute(sql,val)
#mydb.commit()    #数据表有更新，必须commit
#print(mycursor.rowcount,"记录插入成功") #rowcount 表示插入的条数
# 插入数据 #mycursor.lastrowid 表示最后的ID号

#mycursor.execute("select * from sites")
#myresult = mycursor.fetchall() #fetchall() 获取所有记录
#for i in myresult:
#    print(i)
# 数据表的普通查询

#sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites




