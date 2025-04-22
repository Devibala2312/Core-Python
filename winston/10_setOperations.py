def perform_set_operations(set1, set2):
    union_set = set1 | set2
    intersection_set = set1 & set2
    difference_set1 = set1 - set2
    difference_set2 = set2 - set1
    return union_set, intersection_set, difference_set1, difference_set2

final_union_set, final_intersection_set, final_difference_set1, final_difference_set2 = perform_set_operations({'1', '2', '3'}, {'4', '3', '5'})

print('Union set: ', final_union_set)
print('Intersection set: ', final_intersection_set)
print('Difference set1: ', final_difference_set1)
print('Difference set2: ', final_difference_set2)