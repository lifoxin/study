from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)           # 4个进程立刻执行
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))  #异步 apply_async ,默认有 target = func, args 是指定函数的元组参数
    print('Waiting for all subprocesses done...')
    p.close()  #不能添加新进程
    p.join()   #等待子进程执行完毕
    print('All subprocesses done.')
