charsToCount = 'google.com'
charCount = {}
for char in charsToCount:
    if char not in charCount:
        charCount[char] = 0
    charCount[char] += 1
print(charCount)


