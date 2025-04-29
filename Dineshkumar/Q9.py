#9. Given a list of words, return a set of words that appear more than once in the list.
def unique_method(word):
    duplicates = set()
    non_duplicates = set()
    for value in word:
        if value in word:
            duplicates.add(value)
        else:
            non_duplicates.add(value)

    return duplicates

list_word = ["Hi" , "Bye", "Hi", "the"]


print(unique_method(list_word))