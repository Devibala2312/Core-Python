sampleTuple = (1, 22, 3)

def double_tuple_elements(tuple_input):
    return tuple(x*2 for x in tuple_input)

print('Final output: ', double_tuple_elements(sampleTuple))