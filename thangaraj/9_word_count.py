listOfWords = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

print({word for word in listOfWords if listOfWords.count(word) > 1})
    
