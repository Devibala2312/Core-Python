# 13. Write a function that takes a tuple of inputNumbers and returns a new tuple with each element doubled

def doubled_tuples(tuple_input):
    tuple_output = [2 * x for x in tuple_input]
    print(tuple_output)

doubled_tuples((1, 2, 3, 4, 5, 6))
