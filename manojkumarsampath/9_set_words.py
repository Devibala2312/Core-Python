#9. Given a list of words,
# return a set of words that appear more than once in the list.

def find_duplicates(words):
    seen = set()
    duplicates = set()
    for word in words:
        if word in seen:
            duplicates.add(word)
        else:
            seen.add(word)
    return duplicates

# Example usage
word_list = ['apple', 'banana', 'cherry', 'apple', 'banana', 'date']
print(find_duplicates(word_list))
