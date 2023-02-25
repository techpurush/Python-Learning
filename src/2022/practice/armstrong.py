num = 154
t = num
s = 0
while (num > 0):
    r = num % 10
    p = r ** 3
    s += p
    num = num // 10

if (int(t) == int(s)):
    print("{} is armstrong number.".format(t))
else:
    print("{} is not armstrong number.".format(t))
