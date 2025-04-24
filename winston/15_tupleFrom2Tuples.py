tuple1 = (1, 2, 3)
tuple2 = (4, 3, 5, 6, 1)

def create_tuple_from_two_tuples(tuple_input_1, tuple_input_2):
    return tuple(set(tuple_input_1 + tuple_input_2))

print('Final output: ', create_tuple_from_two_tuples(tuple1, tuple2))