from array import *

arr=array('i',[1,2,4,5,6])

print(arr.pop())
print(arr.append(10))
print(arr.pop())
print(arr.count(1))
print(arr.insert(1,55))
print(arr.remove(5))
print(arr.reverse())
print(arr.tolist())
del(arr[2])
print(arr)

arr2=arr

print(arr2)

