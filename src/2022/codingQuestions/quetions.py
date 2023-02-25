import re


def replaceLowerCase(str):
    print("Original : ",str)
    print(re.sub('[a-z]','',str))

# replaceLowerCase("KASHSDFDSHsdkfbsdkfHeejxfnsNJJJ")

# def insertSpace(str):
#     print("Original : ",str)
#     print(re.sub(r'(\w)([A-Z])',r'\1 \2',str))

# insertSpace('AdityaKumaSharma')


# def deleteParanthesis(str):
#     print("Original : ",str)
#     matches=re.sub(r' \([\S]+\)','',str)
#     print(matches)
#     # print(re.sub(r'(\(.*\)) .*','',str))
#
# deleteParanthesis("example (.com) w3resource github (.com)")

# print(re.findall(r'[A-Z][a-z]*','AAdityaKumarSharma'))
# print(re.sub(r'\s+',' ','aditya kumar  sharma            ,Hi'))
# print(re.findall(r'"(.*?)"','"aditya" "Kumar","Sharma"'))

# import heapq
# l=[1,2,3,1,3,5,2,5,56321,0,3453,34,2,21]
# heapq.heapify(l)
# print(heapq.nlargest(2,l))
# print(heapq.nsmallest(2,l))

nums='acode'

# print(sorted(nums[0:4]))
# while True:
#     del(nums[nums.index(6):nums.index(7) + 1])
#
#     if 6 not in nums:
#         break
#
# for i in range(0, len(nums)):
#     if nums[i] == 6:
#         start = i
#     if nums[i] == 7:
#         end = i
#
#     if start != -1 and end != -1 and end > start:
#         # del(nums[start:end+1])
#         lst.append(str(start) + "-" + str(end))
#         start = -1
#         end = -1
# else:
#     break

# print(nums)

num=-123
# print(''.join(list(reversed(str(abs(num))))))

text='the lazy dog jumped over the quick brown fox'

str1='a'

# print(ord(str1))
# import string
# for i in text:
#     if i==' ':print(i,end='')
#
#     if i=='z': print('b',end='')
#     elif i=='y': print('a',end='')
#     else:
#         if i in string.ascii_lowercase:
#             print(chr(ord(i)+2),end='')

# print('\n'.join(sorted(dir(__builtins__))))

import random
print(random.randrange(100000,999999))

str1 = 'My Name is Jessa'

lst=[''.join(list(reversed(x))) for x in str1.split()]
print(lst)

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}

dict1={}
for k,v in ascii_dict.items():
    dict1[v]=k

print(dict1)

from collections import Counter

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]

lst=[k for k,v in Counter(sample_list).items() if v>1]

print(lst)

# Dictionary
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}

# Filter dict using following keys
l1 = ['A', 'C', 'F']

lst= {key:d1[key] for key in l1}

print(lst)

currentEmployee = {1: 'Scott', 2: "Eric", 3:"Kelly"}
formerEmployee  = {2: 'Eric', 4: "Emma"}

allEmployee = {**currentEmployee, **formerEmployee}
print(allEmployee)

import string
import itertools
def get_row_col(str1):
    gy=itertools.groupby(str1)
    # sorted(gy)
    lst=[]
    for k,g in gy:
        # print(k," : ",list(g))
        if k=='0':
            lst.append(len(list(g)))

    # sorted(dic)

    print(sorted(lst,reverse=True)[0])

import ast
def is_valid_python(code):
   try:
       ast.parse(code)
   except SyntaxError as e:
       print(e)
   return True

is_valid_python('1 /// 2')