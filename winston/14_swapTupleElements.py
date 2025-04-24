names = ('Mirror', 'Tree', 'Car')

def swap_values(input_tuple):
    #converting to a list since tuple is immutable
    input_tuple = list(input_tuple)
    input_tuple[0], input_tuple[-1] = input_tuple[-1], input_tuple[0]
    return input_tuple

print('Swapped names: ', swap_values(names))