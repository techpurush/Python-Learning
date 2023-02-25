def sayHello(name='Sam'):
    print(f'hello {name}')

# sayHello()

def getSum(num1,num2):
    total=num1+num2
    return total

value=getSum(3,4)
# print(value)

getAverage = lambda num1,num2:int((num1+num2)/2)

print(getAverage(2,4))