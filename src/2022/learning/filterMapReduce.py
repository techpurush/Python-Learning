nums = (2, 1, 3, 5.5, 5, 6, 7, 7)

print(list(filter(lambda n: n % 2 != 0, nums)))

print(list(map(lambda x: 2 * x, nums)))

from functools import reduce

print(reduce(lambda a, b: a + b, nums))

import collections
import functools
import itertools

print(list(itertools.accumulate(nums,lambda x,y:x*y)))

# print(help(itertools))
