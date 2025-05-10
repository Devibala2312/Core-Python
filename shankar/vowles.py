def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Example usage
input_string = "Hello, how are you?"
print(f"Number of vowels: {count_vowels(input_string)}")
