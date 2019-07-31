def da(day):
    if day==1:
        return 1
    else:
        return (da(day-1)+1)*2
xli=[da(n) for  n in range(10,0,-1)]
print(xli)