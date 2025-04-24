#15. Write a function that takes two tuples and returns a new tuple that
# contains all elements from both tuples without any duplicates.

def merge_tuple(t1, t2):
    return tuple(set(t1 + t2))

a = (1, 2, 3)
b = (3, 4, 5)
result = merge_tuple(a, b)
print(result)
