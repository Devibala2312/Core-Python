def combine_tuples(a, b):
    new_tuple = set(a) | set(b)
    return tuple(new_tuple);
tuple_1 = tuple(map(int, input("Enter tuple 1:").split()))
tuple_2 = tuple(map(int, input("Enter tuple 2:").split()))
print(combine_tuples(tuple_1, tuple_2))