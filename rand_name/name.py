
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

num = random.randint(1,2)

def Boyname():
   # name =  random.choice(firstname) + "".join(random.choice(boyname) for i in range(2))
    num = random.randint(1,2)
    name = "李" + "".join(random.choice(boyname) for i in range(num))
    print(name)

def Girlname():
    name = random.choice(firstname) + "".join(random.choice(girlname) for i in range(num))
    print(name)

if __name__ == "__main__":
    
    Boyname()   
    Girlname()
   
