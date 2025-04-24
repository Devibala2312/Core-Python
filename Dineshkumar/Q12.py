#12. Create a dictionary comprehension that maps each word in a list to its length.
dict_value = {}
def mapping_words (list_one):
    for word in list_one:
        dict_value[word] = len(word)
    return dict_value


list_of_string = ["Yellow", "Red", "Green", "Blue"]
print(mapping_words(list_of_string))
