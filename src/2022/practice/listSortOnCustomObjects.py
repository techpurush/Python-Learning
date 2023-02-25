import datetime
import pprint
class Person(object):
    def __init__(self,name,bday,height):
        self.name=name
        self.bday=bday
        self.height=height
    def __repr__(self):
        return self.name

data=[
    Person('Kunal',datetime.date(1992,5,22),176),
    Person('Aditya',datetime.date(1995,8,27),172),
    Person('Saksham',datetime.date(1995,7,27),174)
]
data2=[
{"name":'Kunal',"bday":datetime.date(1992,5,22),"height":176},
{"name":'Aditya',"bday":datetime.date(1995,8,27),"height":172},
{"name":'Saksham',"bday":datetime.date(1995,7,27),"height":174}
]

data2.sort(key=lambda item:item['bday'])
pprint.pprint(data2)

# ---------------------------------------------------------------------
# !/bin/python3

import math
import os
import random
import re
import sys


# def swap(dic,s,e):

if __name__ == '__main__':
    s = input()
    from collections import *

    l = re.findall(r'\w', s)
    d = Counter(l)
    l = [[item, key] for item, key in d.items()]

    l = sorted(l, key=lambda x: (x[0]), reverse=False)
    l = sorted(l, key=lambda x: (x[1]), reverse=True)

    for i in range(0, 3):
        print(l[i][0], l[i][1])

