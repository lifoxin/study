#!/usr/bin/env python3

#把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 

class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self
               
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration   #StopIteration 异常用于标识迭代的完成
       
                             
myclass = MyNumbers()        #实例化类对象
myiter = iter(myclass)       #生成迭代器的下一个元素
                           
for x in myiter:
    print(x)
