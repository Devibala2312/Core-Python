# 18. Write a program to count the number of
# vowels in a string using membership operators (in)

# Input from the user
text = "sample"

# Initialize a counter
vowel_count = 0
vowels = "aeiouAEIOU"

# Loop through each character in the string
for char in text:
    if char in vowels:
        vowel_count += 1

# Output the result
print(f"The number of vowels in the string is: {vowel_count}")