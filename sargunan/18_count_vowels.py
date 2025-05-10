# 18. Write a program to count the number of vowels in a string using membership operators (in)

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

string = "Hello"
print(count_vowels(string))