#!/usr/bin/env python3

import random

def bubbleSort(list):
    '''
    以下方法是冒泡排序，如果原来是正常排序，就只需排序一次
    '''
    for j in range(len(list)-1):
        count = 0
        for i in range(len(list)-1-j):
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
                count += 1
        if count == 0:
            return 

if __name__=="__main__":
    
    while True:
         arr = range(100)
         list = random.sample(arr,10)  # 随机选取0-99的10个数字
         print("原来的列表：",list)
         bubbleSort(list)              #实例化方法之后，list应该正常排序
         print("之后的列表：",list)
         if input("空格继续，按q退出:") == 'q':
             break
