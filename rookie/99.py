#!/usr/bin/env python3

i,j = 1,1

print("\n----------------------9x9乘法表-------------------------\n")
for i in range(1,10):
    for j in range(1,i+1):
        print("{}x{}={}\t".format(j,i,i*j),end="")
    print()
