def checkAnagram(str1, str2):
    if len(str1) == len(str2):
        str1 = sorted(str1.lower())
        str2 = sorted(str2.lower())
        if str1 == str2:
            return True
        else:
            return False
    else:
        return False

print(checkAnagram("care",'race'))
