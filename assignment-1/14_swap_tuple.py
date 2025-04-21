# swap first and last element of tuple

def swap_first_last(x):
    return x[-1:] + x[1:-1] + x[:1]

print(swap_first_last((1,2,3,4,5)))

