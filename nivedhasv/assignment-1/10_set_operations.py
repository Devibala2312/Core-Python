# 10. Given two sets, write a function to return their union, intersection, and difference.

def set_operations(set1,set2):
    return f'Union: {set1.union(set2)}\nIntersection: {set1.intersection(set2)}\nDifference: {set1.difference(set2)}\nSymmetric Difference: {set1.symmetric_difference(set2)}'

print(set_operations({1,2,3},{4,5,6,3}))

