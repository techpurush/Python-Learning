import functools
import operator

#def fun1(n):
#
#     if n == 0:
#         return
#
#     # print(n)
#     fun1(n-1)
#     print(n)
#
# fun1(5)

# def fun2(n,s=0):
#
#     if n==0:
#         # s=s+i
#         # print(s)
#         return s
#
#     s=s+n
#     # print(s)
#     val=fun2(n-1,s)
#
#     return val
#
#     # return s
#
# print(fun2(5))

# print(val)

# def fun3(n):
#
#     if n==1 or n==0:return 1
#
#     fact=n*fun3(n-1)
#
#
#     return fact
#
# print(fun3(5))



# def fun4(n,a=0,b=1,items=[]):
#
#     if n==0:
#         print(items)
#         return functools.reduce(operator.add,items)
#
#     # print(a,end=" ")
#     items.append(a)
#
#     a,b=b,a+b
#
#     return fun4(n-1,a,b)
#
# print(fun4(5))

# def fun5(x,n):
#
#     if n==0: return 1
#     if n==1: return x
#
#     val=x*fun5(x,n-1)
#
#     return val
#
# print(fun5(2,3))





