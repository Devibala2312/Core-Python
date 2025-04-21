# count the number of characters in a string.

def count_chars(str1):  
    strDict = {}
    for x in str1:
        if x not in strDict.keys():
            strDict[x] = 1
        else:
            strDict[x] += 1
    return strDict

print(count_chars("google.com"))
