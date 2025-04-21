#find duplicate words in a list

def find_duplicate_words(list1):
    dict_of_words = {}
    for x in list1:
        if x not in dict_of_words.keys():
            dict_of_words[x] = 1
        else:
            dict_of_words[x] += 1

    new_set = set()
    for x in dict_of_words.keys():
        if dict_of_words[x] > 1:
            new_set.add(x)

    return new_set

print(find_duplicate_words(['abc', 'xyz', 'aba', '1221', 'xyz', '1221']))