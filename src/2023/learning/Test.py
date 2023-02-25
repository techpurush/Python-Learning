import traceback

try:
    a = 1
    b = 2
    print(a == b)
    print(b == c)
except Exception as e:
    # print('exception1: ',er.__class__)
    # print('exception1: ',sys.exc_info())

    print(traceback.format_exc())

else:
    print('no error')
