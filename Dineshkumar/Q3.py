# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead the empty string\

def string_of_word(word):
    if len(string_word) > 2:
        return string_word[0]+ string_word[1] + string_word[-2] + string_word[-1]
    else: return "Empty String"

string_word = input("Enter a word: ")
print(string_of_word(string_word))
