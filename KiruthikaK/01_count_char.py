input_text = "python assessment"
dict = {}
for letter in input_text:
    if letter not in dict.keys():
        dict[letter] = 1
    else:
        dict[letter] += 1
print(dict)