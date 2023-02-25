x=12
y=45

if(x>50 and y>50):
    print("greater than 50 (x,y->{x}{y})".format(x=x,y=x))
elif y>40:
    print("y is greater than 40")
else:
    print("Invalid values")

numbers =[23,4,5,6,45]

if(x in numbers):
    print("True")
else:
    print("False")

if not(x==y):
    print("Equal")


if(x not in numbers):
    print("True")
else:
    print("False")


if(x is not y):
    print("True")
else:
    print("False")
