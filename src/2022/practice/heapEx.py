import heapq
import datetime
import pprint




class Person(object):
    def __init__(self,name,bday,height):
        self.name=name
        self.bday=bday
        self.height=height
    def __repr__(self):
        return self.name+" "+str(self.bday)+" "+str(self.height)


data=[
    Person('Kunal',datetime.date(1992,5,22),177),
    Person('Aditya',datetime.date(1995,8,27),172),
    Person('Saksham',datetime.date(1995,7,27),171)
]
data2=[
{"name":'Kunal',"bday":datetime.date(1992,5,22),"height":176},
{"name":'Aditya',"bday":datetime.date(1995,8,27),"height":172},
{"name":'Saksham',"bday":datetime.date(1995,7,27),"height":174}
]

# longest=heapq.nsmallest(1,data2,key=lambda item:item['height'])
# longest=heapq.nlargest(1,data,key=lambda item:item.height)

# print(longest)

numbers=[99,234,435,5656,76,56]

# print(heapq.nlargest(2,numbers))
# print(heapq.nsmallest(2,numbers))

heapq.heapify(numbers)
print(numbers)
print(heapq.heappop(numbers))