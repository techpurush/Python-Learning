def pal(s):
    l=len(s)
    arr=[[0 for i in range(l)] for j in range(l)]
    import pprint
    # pprint.pprint(arr)
    l = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if(i==j):
                arr[i][j]=1
                l.append(s[i])

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if(i==j-1):
                if s[i]==s[j]:
                    arr[i][j]=1
                    l.append(s[i:j+1])
                else:
                    arr[i][j]=0
    # pprint.pprint(arr)

    # for

    for k in range(len(arr)-2):
        i=0
        for j in range(k+2,len(arr[0])):

            if s[i]==s[j] and arr[i+1][j-1]==1:
                arr[i][j]=1
                l.append(s[i:j+1])
            else:
                arr[i][j]=0
            i=i+1
    l.sort(key=len,reverse=True)
    print(l)




pal('abcda')

# from decimal import *
# print(Decimal('-123.23').copy_sign('122'))