inpArrival=  '9:00, 9:40, 9:50, 11:00, 15:00, 18:00'
inpDeparture='9:10, 12:00, 11:20, 11:30, 19:00, 20:00'
st=''
arr1=list(map(lambda x:int(x.replace(':','').strip()),inpArrival.split(',')))
arr2=list(map(lambda x:int(x.replace(':','').strip()),inpDeparture.split(',')))
arr1.sort()
arr2.sort()
s=len(arr1)

# arr = [100, 300, 500]
# dep = [900, 400, 600]

# Brute Force
def neededPlatform(arr,dep,n):
    res=needed=1
    for i in range(n):
        needed=1
        for j in range(i+1,n):
            if arr[i]< arr[j] <dep[i]:
                needed+=1

        res=max(needed,res)

    return res



# Optimised
def minPlatform(arr,dep,n):
    res=needed=1
    i=1
    j=0

    while(i<n and j<n):
        if(arr[i]<=dep[j]):
            needed+=1
            i+=1

            if needed>res:
                res=needed
        else:
            needed-=1
            j+=1

    return res
print(neededPlatform(arr1,arr2,s))

