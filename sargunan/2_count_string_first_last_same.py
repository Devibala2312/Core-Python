# Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.

string_list = ['abca', 'xyz', 'aba', '1221', 'aa', 'b']

count = 0
for s in string_list:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print("Number of strings with length >= 2 and same first and last character: ", count)