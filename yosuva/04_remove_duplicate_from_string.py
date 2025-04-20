# remove duplicate characters from a string

def remove_duplicate(str1):
    str2 = str1[0]

    for x in range(1, len(str1)):
        if str1[x] not in str2:
            str2 += str1[x]
    return str2

print(remove_duplicate('aabbccdffdeaaaa'))
