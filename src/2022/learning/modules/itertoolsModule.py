from itertools import *

inp=[i for i in range(1,10)]
inp2=[i for i in range(10,15)]
print(inp)
print(inp2)
b=permutations(inp,2)

# print((list(b)))

# for t in zip_longest(inp,inp2,fillvalue="-"):
#     a,b=t
#     print(a," ",b)

print("-"*20)

# lst = [("a", 5, 6), ("b", 2, 4), ("a", 2, 5), ("c", 2, 6)]
# groups=groupby(lst,key=lambda x:x[2])
# for k,group in groups:
#     print(k," : ",list(group))


# c=1
# for i in cycle("abcd"):
#     print(i)
#     c+=1
#     if(c is 100):
#         break

c=count()