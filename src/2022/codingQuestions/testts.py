import itertools
from fractions import Fraction
print (Fraction(16, -10))

print (Fraction(123))

print (Fraction())

print (Fraction('3/7'))

print (Fraction(' -3/7 '))

print (Fraction('1.414213 \t\n'))

print (Fraction('-.125'))

print (Fraction('7e-6'))

print (Fraction(2.25))

print (Fraction(Fraction.from_float(1.1)))

from decimal import Decimal
print (Fraction(Decimal('1.1')))

# print(dir(Fraction))
txt="orting"
txt=''.join(sorted(txt))
print(txt)

import re
print(re.match("c", "abcdef"))    # No match
match=re.search("c", "abcdef")
print(match.group())   # Match

l=[20,100,10,12,5,13]
print(list(itertools.combinations(l,3)))