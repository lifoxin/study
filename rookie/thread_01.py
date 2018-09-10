#!/usr/bin/env python3

import _thread
import time

def print_time(threadName,delay):
    count = 0
    while count <5:
        time.sleep(delay)
        count+=1
        print('{}:{}'.format(threadName,time.ctime(time.time())))

while True:
    try:
        _thread.start_new_thread(print_time,("thread-1",1))
        _thread.start_new_thread(print_time,("thread-2",2))
    except:
        print("error:无法启动线程")
   
   input("任意键继续：")
