listOfWords = ['Sand', 'Mirror', 'Tree', 'Mirror', 'Car', 'Rock', '']

repeatingWords = {}

for i in listOfWords:
    if i in repeatingWords:
        repeatingWords[i]+= 1
    else:
        repeatingWords[i] = 1

print(repeatingWords)

finalList = []

for key, value in repeatingWords.items():
    if value > 1:
        finalList.append(key)

print('The words that are repeating more than once: ', finalList)