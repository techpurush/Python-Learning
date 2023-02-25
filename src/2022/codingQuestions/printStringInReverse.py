def printRev(str1,idx):

    if idx==-1:return

    print(str1[idx],end="")

    printRev(str1,idx-1)

    return

printRev("abcd",len("abcd")-1)




