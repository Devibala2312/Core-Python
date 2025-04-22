# 18. Write a program to count the number of vowels in a string using membership operators (in)

def count_vowels(input_string):
    vowels = 'aeiou'
    count = 0
    for ch in input_string:
        if ch in vowels:
            count +=1
    return count

print(count_vowels('haitharali'))