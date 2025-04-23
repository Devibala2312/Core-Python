#2. Write a Python program to count the number of strings where the string length is 2
# or more and the first and last character are same from a given list of strings.


sample_list = ['abc', 'xyz', 'aba', '1221']
count = 0
for value in sample_list:
    if len(value) >= 2 and value[0] == value[len(value) - 1]:
        count += 1
print(count)