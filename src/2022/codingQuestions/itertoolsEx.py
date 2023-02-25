import itertools

for i in itertools.count(5,5):
    if i ==35:
        break
    else:
        print(i,end=" ")

count=0
for i in itertools.cycle('AB'):
    if count>7:break
    else:
        print(i)
        count+=1

iter=itertools.cycle(['hello','aditya'])

print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

import random

val=list(itertools.repeat(random.randint(1,100),10))    
print(val)
