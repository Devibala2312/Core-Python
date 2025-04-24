# Write a program to count the number of vowels in a string using membership operators (in)

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def count_vowels(input_string):
    count = 0
    for chr in input_string:
        if chr in vowels:
            count += 1
    return count

print('Total no. of vowels in the given String is: ', count_vowels('Mirror'))