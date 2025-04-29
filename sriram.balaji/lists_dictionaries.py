# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 12:06:40 2025

@author: sriram.balaji
"""

## tuples input of integer and return the same tuple doubled.

input_tuple = (1,2,5,7,8,2356)

def doubleTuple(originalTuple: tuple):    
    return originalTuple + originalTuple


result_set = doubleTuple(input_tuple)

print('Doubled Tuples : ', result_set)
print('Type of result_set', type(result_set))
    

##Swap first an last elems of tuple

first_tuple = (1,3,5,5786,970,3532)

def swapElemsTuple(val: tuple):
    if len(val) < 2:
        return val
    return (val[-1],) + val[1:-1] + (val[0],)


final_val = swapElemsTuple(first_tuple)

print('Swapped Tuples : ', final_val)
print('Type of final_val', type(final_val))



###Merge two tuples

t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)

def merge_unique_tuples(tuple1, tuple2):
    return tuple(set(tuple1 + tuple2))


result = merge_unique_tuples(t1, t2)
print(result)









