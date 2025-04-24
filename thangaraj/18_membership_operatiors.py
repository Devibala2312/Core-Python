givenString = "Hello World"
vowels = "aeiou"
vowelCount = 0

for char in givenString:
    if char in vowels:
        vowelCount += 1

print(vowelCount)


