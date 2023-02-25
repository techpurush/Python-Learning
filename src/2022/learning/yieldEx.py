def getFib():
    a,b=0,1
    for i in range(10):
        yield a
        a,b=b,a+b

print([i for i in getFib()])
# print(getFib())
def fun1():
    yield 1
    yield 2
    yield 3

nums=fun1()
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums,None))

# for x,y in zip(getFib(),nums):
#     print(x,y)
