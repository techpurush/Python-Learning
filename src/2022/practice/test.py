import keyword

# for item in keyword.kwlist:
#     print(item)

a, b, _ = 1, 2, 3
print(a,b)
print(True==0)

# text='abcde'
# text=b'a'

# print(text)
# print(type(text))
# print(list(text))

# a=b'a'
# print(ord(a))
byte=b''
for x in range(ord('a'),ord('z')+1):
    # print(chr(x))
    # chars.append(chr(x))
    byte+=bytes(chr(x),'ascii')


string =byte.decode('utf-8')
print(list(byte))
print(list(string))

# print(string)

print(b'aditya\nkumar')

str='hello'
print(id(str))
str+='hi'
print(id(str))

alphas=list(string)
print(alphas.pop())
print(alphas)

"""This is a doc string"""
"Simple string"
tup=tuple(['aditya'])
print(tup)

from math import pow as p
print(p(2,3))

for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, '::', item)

x = map(lambda e : e.upper(), ['one', 'two', 'three', 'four'])
print(list(x))

dict1={"a":1,"b":2}

for k in dict1:
    print(dict1[k])

