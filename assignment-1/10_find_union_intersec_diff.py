#find union, intersection and difference of two sets

def find_set_union_intersection_difference(set1, set2):
    union = set1.union(set2)
    intersection = set1.intersection(set2)
    difference = set1.difference(set2)
    return union, intersection, difference

print(find_set_union_intersection_difference({1, 2, 3, 4, 5}, {3, 4, 5, 6, 7}))
