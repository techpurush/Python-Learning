import json

obj2 = {'name': 'Aditya', 'age': 26, 'work': 'IT'}

jdump = json.dumps(obj2)

print(jdump)


jobj=json.loads(jdump)

print(jobj['name'])
