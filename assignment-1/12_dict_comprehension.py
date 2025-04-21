#dict comprehension

words = ["apple", "banana", "cherry"]

dict_of_words = {x:len(x) for x in words}

print(dict_of_words)


