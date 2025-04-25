# 18. Write a program to count the number of vowels in a string using membership operators (in)

def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello world"))
print(count_vowels("python programming"))
print(count_vowels("machine learning"))

