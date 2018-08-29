#!/usr/bin/env python3

import sys   #导入 sys 模块

list=[1,2,3,4]
it = iter(list)   #创建迭代器对象

while True:
    try:
        print(next(it))
    except:
        sys.exit()
