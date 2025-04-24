letters = input("Enter a string: ")
count ={}
for letter in letters:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1
print(count)