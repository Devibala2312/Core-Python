#find common elements in two lists

def find_common(list1, list2 ):
    return set(list1) & set(list2)

print(find_common([1, 2, 3, 4, 5], [3, 2, 1, 9, 8]))
