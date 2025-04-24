name = "google.com"

char_count = {}

for char in name.lower():
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Approach 1:
print('The character occurrences are: ', char_count.items())

# Approach 2
print("The character occurrences are:")
for char, count in char_count.items():
    print(f'The char {char} has occurred {count} time(s)')