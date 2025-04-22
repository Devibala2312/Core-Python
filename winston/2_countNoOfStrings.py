sampleList = ['abc', 'xyz', 'aba', '1221']

count = 0

for str in sampleList:
    stringLength = len(str)
    if stringLength >= 2 and str[0] == str[stringLength-1]:
        print('{str} is TRUE')
        count+= 1
    else:
        print('{str} is FALSE')


print("Total count of Strings: ", count)