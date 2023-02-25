def printSubSequence(str1, idx=0, sub='', lst=[]):
    if idx == len(str1):
        # print(sub)
        lst.append(sub)
        return

    char1 = str1[idx]

    printSubSequence(str1, idx + 1, sub + char1, lst)
    printSubSequence(str1, idx + 1, sub, lst)

    return sorted(list(filter(None, set(lst))))


import re

# data = [int(x) for x in printSubSequence('123')]
for d in printSubSequence('123'):
    print(' '.join(re.split('', d)).strip())
