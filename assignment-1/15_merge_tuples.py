# merge tuples

def merge_tuples(x,y):
    new_set = set(x+y)
    return tuple(new_set)

print(merge_tuples((1,2,3), (4,5,6,3)))

