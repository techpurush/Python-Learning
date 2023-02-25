course="Python \"Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])

print(course[:])

# Formatted String
first="aditya"
last="kumar"
full=f"{first} {last} : {len(first+last)} -> {len(first+last) == 0}"
print(full)

# String Methods
print(first.upper())
print(first.lower())
print(full.title())
print(full.capitalize())
print(first.isalpha())
print(first.isascii())
print(first.strip())
print(first.index('y'))
print(len(first)-1-first.find('y'))

a="a"
b="A"
print(a.lower()==b.lower())