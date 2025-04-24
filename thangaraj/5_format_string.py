wordsToFormat = ['string', 'hello', 'world', 'thing', 'hi', 'to']
formattedWords = []
for word in wordsToFormat:
    if(len(word) < 3):
        formattedWords.append(word)
    elif(word[-3:] == 'ing'):
        formattedWords.append(word + 'ly')
    else:
        formattedWords.append(word + 'ing')

print(formattedWords)

