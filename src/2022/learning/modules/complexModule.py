import cmath

a=2+3j
b=1-7j

print(a.real,a.imag)
print(abs(a))
print(a.conjugate())

print(a+b)
print(a-b)
print(a*b)
print("{:.1f}".format(a/b))