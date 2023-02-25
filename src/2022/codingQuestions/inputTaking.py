from fractions import Fraction
from functools import reduce
from functools import *


def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)

    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

# ---------------------------------------------------------------------------------------------

def fun(s):
    pass
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

# ---------------------------------------------------------------------------------------------

def merge_the_tools(string, k):
    pass
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)