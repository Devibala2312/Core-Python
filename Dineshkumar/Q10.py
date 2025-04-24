#10. Given two sets, write a function to return their union, intersection, and difference.

def set_operation(list_one, list_two):
    union_set = set(list_one).union(set(list_two))
    intersection_set = set(list_one) & set(list_two)
    difference_set = set(list_one) - set(list_two)

    return union_set, intersection_set, difference_set

list_1 = [6,99,0,2,4,5]
list_2 = [65,99,0,25,4]
result = set_operation(list_1, list_2)
print(result)

