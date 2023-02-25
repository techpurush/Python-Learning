a=10

def fun1():
    a=8
    print(id(globals()['a']))
    print(globals()['a'])
    globals()['a']=15
    print(globals()['a'])
    print(id(globals()['a']))
    print("inside a value: ", a)


fun1()

print("outside id of a: ",id(a))
print("outside a value: ",a)

print("-------------------------------")

def fun2():
    global a
    a=18

fun2()
  
print("value of a: ",a)