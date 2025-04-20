# 9. Given a list of words, return a set of words that appear more than
#  once in the list.

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
    
print(get_duplicate_words(['apple','banana','apple','orange','banana','grape']))
            