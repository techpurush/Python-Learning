import fileinput as fi
import re

inp = []
# for line in fi.input():
#    if re.match(r'\w',line):
#        inp.append(line.rstrip().lstrip())
import sys

# for line in sys.stdin:
#    if re.match(r'\w',line):
#        inp.append(line.rstrip().lstrip())

while True:
   try:
       line=input()
       if re.match(r'\w',line):
           inp.append(line)
   except Exception:
       break


print(inp)