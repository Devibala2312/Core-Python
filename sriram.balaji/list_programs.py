# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 11:31:29 2025

@author: sriram.balaji
"""

##Sorting list of tuple.

input_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

res = sorted(input_list, key=lambda x: x[1])

print('result : ', res)



## list comprehension to square
output_val = [i**2 for i in range(1,20, 1)]
print('Square output : ', output_val)


## min and max from list of integers

list_int = [3,5,7,78,234,89056,123,-2]
list_int.sort()
print(f"min : {list_int[0]}, max : {list_int[-1::]}")