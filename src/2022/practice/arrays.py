from array import *

arr=array('i')
arr.append(5)
arr.insert(0,0)
arr2=array('i',[6,7,8,9])
#arr.extend(arr2)
arr.fromlist([6,7])
arr.remove(6)
print("popped: ",arr.pop())
arr=arr+arr2

print("index of %d: "%5,arr.index(5))

# print(arr.tolist())
# arr.reverse()
arr.append(5)
print(arr.count(5))
print("".join(map(str, arr)))

for i in range(0,len(arr)):
    print(arr[i],end=" ")

print()
arr=array('u',['a','b','c','d'])
arr.fromunicode('j')
print(''.join(arr.tolist()))

# print("-"*10,"Multi Dimensional Array","-"*10)
dict1={"a":1,"b":2}
print([key for key in dict1])
print(dict1.get('c'))

