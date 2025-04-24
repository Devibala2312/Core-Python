# count the number of vowels in a string

def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

# Example usage
vowel_count = count_vowels("Hello World")
print(f"Number of vowels in the string: {vowel_count}")
