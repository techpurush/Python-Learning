def byValue(x):
    print(id(x))
    x=8
    print(id(x))
    print(x)

p=10
print(p)
print(id(p))
byValue(p)

print("-------------------------------------------")

def byReference(x):
    print(id(x))
    x[0] = 8
    print(id(x))
    print(x)


p=[1]
print(p)
print(id(p))
byReference(p)

