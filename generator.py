#!/usr/bin/env python3

import sys

def fn(n):    #生成器函数
    a,b,counter = 0,1,0
    while True:
        if (counter > n):
            return
        yield a  #遇到yield时，函数会暂停并保存当前所有的运行信息
        a,b = b,a+b  #返回yield值，并在下一次执行next()方法时从当前位置继续运行
        counter += 1

f = fn(10)

while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()

