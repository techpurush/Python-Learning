a=5
b=0

try:
    print("Open")
    c=a/b
    print(c)
except Exception as e:
    print("Error: ",e)
finally:
    print("Closed")