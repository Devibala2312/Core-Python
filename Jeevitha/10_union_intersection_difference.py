def set_operations(set1,set2):
    return f'Union: {set1.union(set2)}\nIntersection: {set1.intersection(set2)}\nDifference: {set2.difference(set1)}'

print(set_operations({10,12,23},{40,10,62,23}))