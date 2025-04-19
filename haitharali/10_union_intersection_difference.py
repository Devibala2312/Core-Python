# 10. Given two sets, write a function to return their union, intersection, and difference.

def union_intersection_difference(tuple1: tuple, tuple2: tuple):
    length_tuple1 = len(tuple1)
    length_tuple2 = len(tuple2)
    union_tuple = tuple1 + tuple2
    intersection_sets = {}
    diff_sets = {}
    for i in range(length_tuple1):
        for j in range(length_tuple2):
            if tuple1[i] == tuple2[j]:
                intersection_sets.update(tuple1[i])
            if tuple1[i] != tuple2[j]:
                diff_sets.update(tuple1[i])
    print(union_tuple)
    print(intersection_sets)
    print(diff_sets)


union_intersection_difference((1, 2, 3, 4), (5, 6, 1, 7, 8, 2, 3))
