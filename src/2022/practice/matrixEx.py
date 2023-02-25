from pprint import pprint as print
def transpose(mat):
    nr=len(mat)
    nc=len(mat[0])
    t=[]
    for i in range(nc):
        row=[]
        for j in range(nr):
            row.append(mat[j][i])
        t.append(row)
    return t

mat=[
    [1,2,3],
    [4,5,6]
]

print(mat)
t_mat=transpose(mat)
print(t_mat)