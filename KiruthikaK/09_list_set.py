from collections import Counter
duplicates = lambda x: {x for x, count in Counter(x).items() if count > 1}
# word= ['apple', 'banana', True, 'apple', 'date', 'banana',True,1,2,3,1,(1,2),(1,1),(2,1),(1,2),(1,)]
word= ['apple', 'banana', 'apple', 'date', 'banana',1,2,3,1,(1,2),(1,1),(2,1),(1,2),(1,)]

print(duplicates(word))  # Output: {'banana', 'apple'}

