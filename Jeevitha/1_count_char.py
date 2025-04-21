text = "google.com"
dict = {}
for letter in text:
    if letter not in dict.keys():
        dict[letter] = 1
    else:
        dict[letter] += 1
print(dict)