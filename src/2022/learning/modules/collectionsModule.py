from collections import *
string="Aditya"
counts=Counter(string.lower())

counts[0]

for k,v in counts.items():
    if(v>1):
        print(k," ",v)

# Deque
from collections import *

d=deque('ghi')
d.append('j')
d.appendleft('f')

print(d)
d.rotate(-1)
print(d)