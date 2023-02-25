
# Python variables are case sensitive

'''
This is a multiline comment
for docstring or general purpose.
'''

"""
This is jus a
multiline comment.
"""

x=1
y=2.2

print(x,y,sep="\n")

a,b,c,d,e=(1,2.2,'hi aditya',True,10+2j)

print(a,b,c,d,e)
e=str(e)
print(e)
b=int(b)
print(b)
b=float(b)
print(b)
print(type(e))


print('-----------------------------')

name='aditya'
age=18

val1='hi my name is '+name+' and my age is '+str(age)

print(val1)
print(f'hi I am {name} and my age is {age}')
print('hello my name is {name} and age is {age}'.format(name=name,age=age))

print('-----------------------------')

print(val1.find('aditya'))