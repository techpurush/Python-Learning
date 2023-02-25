
a:int="aditya"
a='aditya'
a="""
aditya 
kumar
"""

# print(a)

a,b=1,2

a=b=10

print(a,b,sep="")


a="1111"
print(a)
print(int(a))
print(int(a,2))
print(float(a))

# ord() - converts to integer ascii value
b='a'
a=ord('a')
print(f"integer ascii value of {b}: ",a)

# hex() - this converts integer to hexadecimal
b=10
a=hex(b)
print(f"hex value of {b}: ",a)

# oct() - this converts integer to octal
b=10
a=oct(b)
print(f"oct value of {b}: ",a)

# tuple() - this converts to a tuple
s="aditya"
a=tuple(s)
print(a)
print(type(a))

# set() - this converts to a set
s="aditya"
a=set(s)
print(a)
print(type(a))

# list() - this converts to a list
s="aditya"
a=list(s)
print(a)
print(type(a))

# dict() - this converts tuple(x,y) into a dictionary
# initializing tuple
tup = (('a', 1) ,('f', 2), ('g', 3))
a=dict(tup)
print(a)
print(type(a))

# complex() - This function converts real numbers to complex(real,imag) number.
a = 1
b = 2
# c=complex("10+12j")
c=complex(a,b)
print(c)
print(type(c))