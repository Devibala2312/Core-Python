list = input('Enter a list of string: ').split()
result = [letter for letter in list if len(letter) >= 2 and letter[0] == letter[-1] ]
print(len(result))

