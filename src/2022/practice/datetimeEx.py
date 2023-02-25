import datetime
import collections
import functools
import itertools
import string
import random
import sys
import re
import time

date=datetime.date
today=date.today()
print(today.year)
print(today.month)
print(today.day)
print(today.strftime("%A, %d %B %Y"))
today2=today.replace(year=today.year+1,month=today.month+2,day=today.day+3)
print(today2.strftime("%A, %d %B %Y"))
bday=date.fromisoformat('1995-08-27')
print(bday.strftime('%A, %d %B %Y'))
print(bday.weekday())
print(bday.isoweekday())
print('-'*5," time ","-"*5)
t=datetime.time(9,30,45,100000)
print(t)

