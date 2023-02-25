import itertools

def printPermutations(str):
    perms=itertools.permutations(str)
    lst=[''.join(p) for p in perms]
    print(lst)
    return

def printPermutations2(str,idx=0):

    if idx==len(str):print(''.join(str))

    for j in range(idx,len(str)):
        words=[c for c in str]

        words[idx],words[j]=words[j],words[idx]

        printPermutations2(words,idx+1)


printPermutations2('pyu')