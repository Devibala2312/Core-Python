# Create a dictionary comprehension that maps each word in a list to its length.

words = ['apple', 'banana', 'cherry']
word_lengths = {word: len(word) for word in words}
print(word_lengths)