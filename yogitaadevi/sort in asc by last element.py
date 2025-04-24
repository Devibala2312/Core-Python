def get_sorted_tuple(tuple):
    return sorted(tuple, key=lambda x: x[-1])
tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(get_sorted_tuple(tuple_list))
