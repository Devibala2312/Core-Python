def get_duplicate_words(list_of_words):
    words_dict = {}
    duplicate_set = set()
    for index in range(len(list_of_words)):
        word = list_of_words[index]
        if(word in words_dict.keys()):
            duplicate_set.add(word)
        else:
            words_dict[word] = 1
    return duplicate_set
    
print(get_duplicate_words(['apple','banana','grapes','orange','apple','banana']))
