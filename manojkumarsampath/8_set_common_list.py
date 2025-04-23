#8. Write a function that takes two lists and returns
# a set of elements that are common to both lists.

def common_elements(list1, list2):
    return set(list1) & set(list2)

# Example usage
a = [1, 2, 3, 4, 5, 7]
b = [4, 5, 6, 7, 8]
print(common_elements(a, b))
