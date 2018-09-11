#!/usr/bin/env python3

import pymysql

#创建数据库对象
db = pymysql.connect("localhost","felix","1","rookie")
#创建游标对象
cursor = db.cursor()
#创建sql语句,查看数据库版本
#sql = "select version()"
#使用execute()执行命令
#cursor.execute(sql)
#使用fetchone()获取单条数据
#data = cursor.fetchone()

#cursor.execute("drop table if exists employee")
#sql = """create table employee(
#         firstName char(20) NOT NULL,
#         lastName char(20),
#         age int,
#         sex char(1),
#         income float) """
#cursor.execute(sql)

#sql = """insert into employee values ('mac','mohan',20,'M',2000)"""
#try:
#    cursor.execute(sql)
#    #更新插入需要commint
#    db.commit()
#except:
#    #回滚
#    db.rollback()

sql = "select * from employee where income > %d" %(100)
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d"% \
               (fname,lname,age,sex,income))
except:
    print("error:ubable to fetch data")


#关闭数据库连接
db.close()



