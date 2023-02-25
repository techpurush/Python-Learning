personDict={

    'name':'aditya',
    'work':"IT",
    'age':26
}

print(personDict.get('name'))

personDict['phone']='0987654321'

print(personDict)

print((personDict.keys()))
print((personDict.items()))
print((personDict.values()))

person2=personDict.copy();

person2['city']='mumbai'


person2.pop('name')

del(person2['work'])

# person2.clear()

print(len(person2))

print(person2)

people=[

    personDict,person2
]

print(people)

print(people[1]['city'])
