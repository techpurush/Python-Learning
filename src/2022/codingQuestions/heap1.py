import heapq
# print(help(heapq))
# l=[23,1,3,54,2,452,5,543,53]
# heapq.heapify(l)
# print(l)
# print(heapq.nlargest(3,l))
# print(heapq.nsmallest(3,l))

class Train:

    def __init__(self,name,arrival,stop,depart,pl):
        self.name=name
        self.arrival=arrival
        self.stop=stop
        self.depart=depart
        self.pl=pl
    def print(self):
        print(self.name,self.arrival,self.stop,self.depart)

    def __repr__(self):
        return self.name+" "+str(self.arrival)+" "+str(self.stop)+" "+str(self.depart)


    def __lt__(self,ot):
        return self.depart< ot.depart

t1=Train('112567',1,2,4,1)
# t3=Train('112563',3,3,7,2)
# t2=Train('112569',4,7,12)
# t4=Train('112560',9,3,13)
l=[t1]
# print(l)
heapq.heapify(l)
x=heapq.nsmallest(1,l)
print(x[0].depart)
if x[0].depart<
# heapq.heappush(t3)


# l=[(2,'balram'),(1,'amit'),(2,'sam')]
# heapq.heapify(l)
# l=heapq.nlargest(2,l)
# print(l)