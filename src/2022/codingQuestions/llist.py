lst=[2,3]

lst.insert(len(lst) if len(lst)>0 else 0,1)
lst.remove()
print(lst)
