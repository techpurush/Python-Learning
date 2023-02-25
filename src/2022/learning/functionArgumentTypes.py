# Keyworded and default argument
def fun1(name,age=18):
    print("Name: ",name)
    print("Age: ",age)

# fun1(name='Aditya')

# Variable length arguments

def fun2(*x):
    for i in x:
        print(i)

# fun2(12,3,4,5,6,'dfd',4.5,4+2j)

# Keyworded variable length arguments

def fun3(**x):
    for k,v in x.items():
        print(k," ",v)

fun3(name='Aditya',age=22)

# Multi value return from a function

def fun4(a,b):
    sum=a+b
    sub=a-b
    return sum,sub

print(fun4(6,5))

# Forcing to pass named parameter
def fun5(*arg,name,age):
    print(name," ",age)
    print(arg)
    return

fun5(12,3,4,name='Aditya',age=27)

