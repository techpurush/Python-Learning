def printFirstLast(str,elementToBeSearched,idx=0,first=-1,last=-1):

    if idx == len(str):
        # print(first," ",last)
        return first,last

    if str[idx] is elementToBeSearched:
        if first ==-1:
            first=idx
        else:
            last=idx

    return printFirstLast(str,elementToBeSearched,idx+1,first,last)


print(printFirstLast("aabcdhsdjkfhsdjkajkfdk",'a'))



