import traceback
try:
    a = 5
    b = 10
    c = a / b
    print("c: ",c)
except Exception as e:
    print("Exception details\n\n: ", traceback.format_exc())
else:
    print("-- No Exception --")
finally:
    print("-- Finally --")
