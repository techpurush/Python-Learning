def makeInc(x):
    def inc(y):
        nonlocal x
        x += y
        return x
    return inc

incOne = makeInc(1)
print(incOne(5))  # returns 6
