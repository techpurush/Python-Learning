def allPermutations(str,sub=''):

    if len(str)==0:
        print(sub,end=" ")


    for i in range(0,len(str)):
        char=str[i]
        newstr=str[0:i]+str[i+1:]
        allPermutations(newstr,sub+char)

str='aditya'
# print(str[0:0])
allPermutations(str)