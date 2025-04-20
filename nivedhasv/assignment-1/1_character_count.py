# 1.Write a Python program to count the number of characters in a string.
text = "My First Python Code block"
letter_dict = {}
for letter in text:
    if letter not in letter_dict.keys():
        letter_dict[letter] = 1
    else:
        letter_dict[letter] += 1
print(letter_dict)

