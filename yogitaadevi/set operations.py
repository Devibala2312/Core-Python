def set_operations(set1, set2):
    return set1.union(set2), set1.intersection(set2), set1.difference(set2), set2.difference(set1)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(set_operations(a, b))
