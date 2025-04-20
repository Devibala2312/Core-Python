# 15. Write a function that takes two tuples and returns a new tuple
# that contains all elements from both tuples without any duplicates.

def combine_tuples(tuple1, tuple2):
    out_tuple = tuple(set(tuple1 + tuple2))
    print("tuple1 ", tuple1,"tuple2" , tuple2)
    print("combined tuples", out_tuple)


combine_tuples((1, 2, 3, 3), (4, 5, 6, 4))
combine_tuples((1,1, 2, 6, 3,7), (4, 5, 6, 4,7,7,8,))