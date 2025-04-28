def merge_unique_tuples(tuple1, tuple2):
    return tuple(set(tuple1+tuple2))

print(merge_unique_tuples((1,3,4,'A',3),(1,2,44,23,1,2,'a')))
