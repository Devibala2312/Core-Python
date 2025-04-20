#count the number of vowels and non-vowels in a string
vowels = "aeiou"

def count_vowels_and_nonvowels(str):
    vowelcount = 0
    nonvowelcount = 0
    for x in str:
        if x in vowels:
            vowelcount += 1
        else:
            nonvowelcount += 1

    return vowelcount, nonvowelcount

print(count_vowels_and_nonvowels("Python"))