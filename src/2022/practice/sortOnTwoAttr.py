dict1=[
    {"Name":"Kunal","Age":28,"Height":172},
    {"Name":"Aditya","Age":27,"Height":170},
    {"Name":"Sameer","Age":28,"Height":174}
]
from pprint import pprint as print

dict1.sort(key=lambda x:(x['Age'],x['Height']),reverse=True)
print(dict1)