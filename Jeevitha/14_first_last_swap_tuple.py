def swap_tuple(tuple_input):
    tuple_input = list(tuple_input)
    tuple_input[0],tuple_input[-1] = tuple_input[-1],tuple_input[0]
    return tuple(tuple_input)

input = (10,0,3,98,-1)
print(swap_tuple(input))