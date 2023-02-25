numbers=[1,2,3,4,5,6,7,8,9]
names=['akash','abhishek','amit','chetan','dharmendra']

# Lambda example
f=lambda x:x[0]

print(f(names))

# Map
wl=map(len,names)
print(list(wl))
wu=map(lambda x:x.upper(),names)
print(list(wu))

import functools
import operator
# Reduce
ns=functools.reduce(operator.add,numbers)
ns=functools.reduce(lambda a,b:a+" "+b,names)
print(type(ns))

# Filter
ns=list(filter(lambda x:x>5,numbers))
print(ns)

nstr='{:~^20}'.format('centered')
print(nstr)

nl=list(map(lambda x:"{:.0%}".format(x), [0.95, 0.75, 1.01, 0.1]))
print(nl)
from operator import *
l1=[1,2,3,4,5]
l2=[2,2,3,4,5]
l3=[3,2,3,4,5]

def average(*args):
    return int(sum(args)/len(args))

print(list(map(average,l1,l2,l3)))