letters = ['a','b','c','b','a','d','c']
print({letters[x] for x in range(len(letters)) if letters[x] in letters[x+1:]})