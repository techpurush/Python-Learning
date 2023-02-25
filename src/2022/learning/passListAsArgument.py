def fun1(x):
    e,o=0,0

    for i in x:
        if(i%2==0):
            e+=1
        else:
            o+=1
    return e,o

print(fun1([1,2,3,4,2,234,2,9]))