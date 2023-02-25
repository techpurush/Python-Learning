def moveAllXToEnd(str,idx=0,sub1=[],sub2=[]):

    if idx==len(str):

        return sub1+sub2

    if str[idx]=='x':
        sub2.append('x')
    else:
        sub1.append(str[idx])

    return moveAllXToEnd(str,idx+1,sub1,sub2)


print(''.join(moveAllXToEnd('axbcxxd')))
