numbers=[1,2,3,4,5,6,7,0,5,0]
names=['Aditya','amit','prabhat','yogesh','','sharan','saksham']

area=lambda x:3.14*pow(x,2)

res=list(map(area,numbers))

print(res)