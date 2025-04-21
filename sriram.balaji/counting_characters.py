# -*- coding: utf-8 -*-
"""
Created on Sun Apr 20 10:03:41 2025

@author: sriram.balaji
"""

val = 'google.com'

my_dict = {}

for i in val:
    print("value of i is {}", i)
    if my_dict.get(i) is None:
        my_dict[i] = 0;
    else:
        my_dict[i] = my_dict.get(i)+1;
        
print('count of characters values : ', my_dict)



####pgm 2 : 

sample_list = ['abc', 'xyz', 'aba', '1221']
result_list = []

for l in sample_list:
    if len(l) >= 2 and l[0] == l[-1::]:
        result_list.append(l);
        
print('List of strings matching conditions : ', result_list)         

    
### pgm 3:
    
str_2 = input('Enter a string more than 2 charaters in length:')

def combine_produce_string_result(val):
    print((val[:2] + val[-2::]) if len(val) > 2 else '')    
        

combine_produce_string_result(str_2)



### pgm 5:
### Adding and ly to String

input_str = input('Enter a string : ');

def addingly(val):
    return val if len(val) < 3 else \
        val + 'ly' if val.endswith('ing') else val + 'ing'

print('result : ', addingly(input_str))







