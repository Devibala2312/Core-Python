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
    

