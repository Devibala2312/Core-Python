# Create a dictionary comprehension that maps each word in a list to its length.

names = ['Winston', 'Manuel', 'Vijay']

finalDict = {name: len(name) for name in names}

print(finalDict)

