def swap_first_last(val):
    return (val[-1],) + val[1:-1] + (val[0],)

val = (1, 2, 3, 4,1.2,1.4,None,False,"awe",'qwe')
print(swap_first_last(val))