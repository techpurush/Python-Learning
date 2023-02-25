from array import *

# row, col = 2, 3
#
# arr = []
#
# Matrix = [[0 for i in range(col)] for j in range(row)]
#
# for i in range(0, row):
#     for j in range(0, col):
#         Matrix[i][j] = i + j
#
#
# print(Matrix)
# print(Matrix.reverse())
# print(Matrix)

image = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(*image)


def getList(*args):
    return list(args)

# Finding the transpose of a matrix using map function
tran=list(map(getList,*image))

print(*tran)

