# Given a list of words, return a set of words that appear more than once in the list.

def find_duplicates(input_list):
    duplicate = set()
    present = set()

    for word in input_list:
        if word in present:
            duplicate.add(word)
        else:
            present.add(word)

    return duplicate

words = ['apple', 'banana', 'cherry', 'apple', 'banana', 'date']
result = find_duplicates(words)
print("Words that appear more than once:", result)