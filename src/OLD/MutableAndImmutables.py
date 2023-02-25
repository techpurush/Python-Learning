# Immutables
x=10
print(id(x))

x=x+1
print(id(x))

# Mutables

print()

list1=[1,2,3]
print(id(list1))

list1.append(4)
print(id(list1))
