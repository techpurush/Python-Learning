def printUniqueSubSequence(str1,idx=0,sub='',lst=[]):

    if idx==len(str1):
        # print(sub)
        lst.append(sub)
        return

    char1=str1[idx]

    printUniqueSubSequence(str1,idx+1,sub+char1)
    printUniqueSubSequence(str1,idx+1,sub)

    return sorted(list(filter(None,set(lst))))


print((printUniqueSubSequence('aaa')))