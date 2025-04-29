def unique_method (list1, list2):
    unique = set(list1 + list2)
    return unique

value1 = (1,5,6,7,7)
value2 = (1,66,6,67,8,9)

result = unique_method(value1, value2)
print (result)