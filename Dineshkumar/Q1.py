# 1.Write a Python program to count the number of characters in a string.

input_string = input("Enter a string: ").lower()
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else: char_count[char] = 1
print ("The character counts are", char_count)

