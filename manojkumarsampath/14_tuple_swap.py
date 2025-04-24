# 14. Write a function that swaps the first and last elements of a tuple.

def swap_tuple(t):
    if len(t) < 2:
        return t
    first = t[0]
    last = t[-1]
    middle = t[1:-1]
    return (last,) + middle + (first,)


original = (7,6,4,5,6,9)
swap = swap_tuple(original)
print(swap)
