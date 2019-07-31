#!/usr/bin/env python3

import random

with open('firstname') as f1:
    firstname = f1.read()
with open('boyname') as f2:
    boyname = f2.read()
with open('girlname') as f3:
    girlname = f3.read()

firstname = firstname.split()
boyname = boyname.split()
boyname = "".join(boyname)
girlname = girlname.replace("\n","").split("、")
girlname = "".join(girlname)

def Boyname():
    num = random.randint(1,2)
    name =  random.choice(firstname) + "".join(random.choice(boyname) for i in range(num))
    print('男孩:{0}'.format(name))

def Girlname():
    num = random.randint(1,2)
    name = random.choice(firstname) + "".join(random.choice(girlname) for i in range(num))
    print('女孩:{0}'.format(name))

if __name__ == "__main__":
    while True:
       	 Boyname()   
         Girlname()
         if input("---------------Enter继续,Q+Enter退出:") == 'q':
            break
            

