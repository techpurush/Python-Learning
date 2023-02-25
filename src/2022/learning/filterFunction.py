numbers=[1,2,3,4,5,6,7,0,5,0]
names=['Aditya','amit','prabhat','yogesh','','sharan','saksham']

# res=list(filter(None,numbers))
# res=list(filter(None,names))
# res=list(filter(lambda x:x>5,numbers))
res=list(filter(lambda x:len(x)<5 and len(x)!=0,names))

print(res)