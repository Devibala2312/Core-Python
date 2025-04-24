# 8. Write a function that takes two lists and returns a set of elements that are common to both lists.


def comon_words(list_one, list_two):
    return  set(list_one) & set(list_two)

list_one = [1,2,3,4,5]
list_two = [11,22,33,4,5]

result = comon_words(list_one, list_two)
print("Common words are" , result)


