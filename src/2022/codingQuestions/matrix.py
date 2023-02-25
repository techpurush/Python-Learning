# from pprint import pprint as pp

# Matrix Print Method
def matPrint(mat):
    for row in mat: print(*row, sep=" ")

m1=[[1,2,3],
    [4,5,6],
    [7,8,9]]

m2=[[1,3,5],
    [2,0,1],
    [4,1,0]]

m3=[]

# Multiplication
for i in range(len(m1)):
    m2c=list(zip(*m2))[i]
    t=[]
    for j in range(len(m1)):
        m1r = m1[j]
        t.append(sum([x*y for x,y in zip(m1r,m2c)]))
    m3.append(t)

matPrint(m3)

# print(m1[0][-1])

# for x,y in zip([1,2,3],[1,2,3]):
#     print(x*y)

# Transpose
# print("Original: ")
# matPrint(m1)
# transposed_mat=list(zip(*m1))
# print("Transposed: ")
# matPrint(transposed_mat)



# Subtract
# for i in range(len(m1)):
#     t=[]
#     for x,y in zip(m1[i],m2[i]):
#         t.append(x-y)
#     m3.append(t)
#
# pp(m3)

# Addition
# for i in range(len(m1)):
#     t=[]
#     for x,y in zip(m1[i],m2[i]):
#         t.append(x+y)
#     m3.append(t)

# pp(m3)


# Transpose
# for i in range(len(m1)):
#     t=[]
#     for j in range(len(m1[0])):
#         t.append(m1[j][i])
#     m3.append(t)

# pp(m3)
