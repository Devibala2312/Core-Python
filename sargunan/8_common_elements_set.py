# Write a function that takes two lists and returns a set of elements that are common to both lists.

def common_elements(list1, list2):
    return set(list1) & set(list2)

print(common_elements([1,2,3,5], [2,5,6,7]))