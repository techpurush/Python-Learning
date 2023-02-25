def checkSorted(arr,idx=0):

    if idx==len(arr)-1: return True

    if arr[idx]>=arr[idx+1]: return False

    return checkSorted(arr,idx+1)

print(checkSorted([1,2,3,4]))
