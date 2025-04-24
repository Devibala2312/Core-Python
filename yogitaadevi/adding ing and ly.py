def modify_string(word):
    if len(word) < 3:
        return word
    elif word.endswith('ing'):
        return word + 'ly'
    else:
        return word + 'ing'

word = input("Enter a word: ")
print(modify_string(word))
