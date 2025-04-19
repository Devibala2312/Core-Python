#2. Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.

my_list = {"abc", "aba", "xyz", "1231", "a"}

for str_value in my_list:
    if len(str_value) >= 2 and str_value[0] == str_value[len(str_value) - 1]:
        print(str_value)
