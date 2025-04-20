# 14. Write a function that swaps the first and last elements of a tuple.

def tuple_swap(input_tuple):
    outputlist = [input_tuple[len(input_tuple)-1]]
    for value in input_tuple[1:-1]:
        outputlist.append(value)
    outputlist.append(input_tuple[0])
    print(outputlist)


tuple_swap((9,1,2,3,4,5,7,8))