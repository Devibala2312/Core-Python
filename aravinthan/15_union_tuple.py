def unionTuple(input1, input2):
    return tuple(set(input1) | set(input2))

print(unionTuple((1,4,5,6),(1,4,8,7)))