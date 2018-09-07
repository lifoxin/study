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
    #name = "李" + "".join(random.choice(boyname) for i in range(num))
    print(name)

def Girlname():
    num = random.randint(1,2)
    name = random.choice(firstname) + "".join(random.choice(girlname) for i in range(num))
    print(name)

if __name__ == "__main__":
    while True:
         Boyname()   
         Girlname()
         if input("---------------任意键继续,q退出:") == 'q':
            break
            

