import random
import random as rd

print(rd.randint(1,5))

nl=[i for i in "aditya"]
print(rd.shuffle(nl))
print(nl)
print(''.join(nl))
print(rd.choice(nl))
from operator import *
print(''.join(list(map(str,[rd.randint(1,10) for i in range(6)]))))