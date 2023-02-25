try:
    data=[1,2,3,4]
    print(5/10)
except Exception as e:
    print("Error: ",e)
else:
    print("No error")
finally:
    print("Close resources here")