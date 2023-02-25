a = 0
b = 1

num = int(input("enter a number: "))

num = num - 2

print(a, " ", b,end=" ")
while (num > 0):
    c = a + b
    print(c, " ",end=" ")
    a, b = b, c

    num = num - 1
