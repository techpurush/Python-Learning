mat = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

for i in range(0,len(mat)):
    for j in range(0,len(mat[0])):
        print(mat[i][j],end=" ")
    print()

print()
print()
for i in range(0,len(mat)):
    for j in range(0,len(mat[0])):
        # t=mat[i][i]
        l=len(mat)
        mat[i][i],mat[i][l-i-1]=mat[i][l-i-1],mat[i][i]
        # mat[i][l - i - 1]=t

for i in range(0,len(mat)):
    for j in range(0,len(mat[0])):
        print(mat[i][j],end=" ")
    print()
