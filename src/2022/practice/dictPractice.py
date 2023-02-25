data={
    "name":"Aditya",
    "roll":12,
    "work":"IT",
    "place":"mumbai"
}

# print(data)

data.update({"place":"BKC, Mumbai","roll":13,"phone":"9900990088"})

# print(data)

# for k,v in data.items():
#     print(k," -> ",v)


v=data.setdefault("roll",15)
# data["roll"]=15
print(v)
# print(data.get('phone2'))
from pprint import *
pprint(data)
