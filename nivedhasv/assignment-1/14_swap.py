
# 14. Write a function that swaps the first and last elements of a tuple.
def swap_tuple(tuple_input):
    tuple_input = list(tuple_input)
    tuple_input[0],tuple_input[-1] = tuple_input[-1],tuple_input[0]
    return tuple(tuple_input)

ip = (1,2,3,4,5)
print(swap_tuple(ip))




