# name,phone=input("Enter name and phone: ").split()

# print("Your name is %s and your phone is %s"%(name,phone))

# numbers=input("enter numbers").split()
# To restrict number of inputs
numbers=input("enter numbers").split()[:4]
data=list(map(float,numbers))
print(data)