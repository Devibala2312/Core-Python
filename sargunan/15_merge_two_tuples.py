# 15. Write a function that takes two tuples and returns a new tuple that contains all elements from both tuples without any duplicates.

def merge_tuple(first, second):
    return tuple(set(first + second))

list1 = (1,2,3,4,5)
list2 = (2,6,3,7,8)
result = merge_tuple(list1, list2)
print(result)