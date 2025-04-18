def swap(input):
    return (input[-1],) + (input[1:-1]) + (input[0],)

print(swap((1,4,5,6)))