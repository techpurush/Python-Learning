import itertools

def printAllCombinations(str1,str2,idx=0):

    if idx==len(str1): return

    char=str1[idx]

    for c in str2:
        print(char,c)

    printAllCombinations(str1,str2,idx+1)

printAllCombinations("abc","def")


