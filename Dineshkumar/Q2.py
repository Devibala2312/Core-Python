# 2. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

list = ["aba", "bbe", "1231", "abc"]
count = 0
for word in list:
     if len(word) >= 2 and word[0] == word[-1]:
        count+=1
print (count)