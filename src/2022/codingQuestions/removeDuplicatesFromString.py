def remDuplicates(str,idx=0,sub=[]):

    if idx==len(str): return ''.join(sub)

    if str[idx] not in sub:
        sub.append(str[idx])

    return remDuplicates(str,idx+1,sub)

print(remDuplicates('abbccda'))