#find the most frequent character in a string

str1 = "programming"
strDict = {}

for x in str1:
    strDict[x] = strDict.get(x,0) + 1

def find_max(arr, n):
    large_num = arr[0]

    for i in range(1, n):
        if arr[i] > large_num:
            large_num = arr[i]
    return large_num

max_number = find_max(list(strDict.values()), len(strDict))

for y in strDict:
    if strDict[y] == max_number:
        print(y)
        break