# 13. Write a function that takes a tuple of inputNumbers and returns a new tuple with each element doubled

def double_tuple(tuple_input):
    return tuple([x*2 for x in tuple_input])

print(double_tuple((1,2,3,4,5)))

