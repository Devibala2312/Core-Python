# 2. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

sampleList = ['abc', 'xyz', 'aba', '1221']

count = 0

for str in sampleList:
    stringLength = len(str)
    if stringLength >= 2 and str[0] == str[stringLength - 1]:
        print(f'The string: {str} passed the expected!')
        count+= 1
    else:
        print(f'The string: {str} failed the expected!')


print("Total count of Strings that passed the expected: ", count)