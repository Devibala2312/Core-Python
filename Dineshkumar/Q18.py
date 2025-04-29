#18. Write a program to count the number of vowels in a string using membership operators (in)

text = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1
print(f"The number of vowels in the given string is {count}")
