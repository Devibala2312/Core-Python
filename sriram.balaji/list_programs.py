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


##Write a python function to return common elements of two lists

list_1 = [1,3,4,5,7,8,9]
list_2 = [10,11,2,4,7,0,5,6]


def commonInList(list1: list, list2: list):
    result_set = set()
    for l in list1:
        if l in list2:
            result_set.add(l)
            
    return result_set

print('common items in list : ', commonInList(list_1, list_2))


##Given a list of words, return set of duplicated words

words = ["word1", "word2", "word3", "word4", "word3", "word2"]

def findDuplicateWords(words: list):
    result_set = set()
    final_set = set()
    for word in words:
        if word not in result_set:
            result_set.add(word)
        else: 
            final_set.add(word)
            
    return final_set

print('duplicates words in list : ', findDuplicateWords(words))


##union, intersection, difference in sets

set1 = {1,2,3,4,5}
set2 = {3,4,6,7,8,9}

def setDifference(set1: set, set2: set):
    return {'union': set1 | set2,
            'intersection': set1 & set2,
            'difference': set1 - set2}

print('Set differnce set: ', setDifference(set1, set2))


##sum of each from list of tuples
tuples_list = [('Alice', 90), ('Bob', 85), ('Alice', 95)]

def summationOfMap(values: list):
    result_map = {}
    for item in values:       
        print('printing item: ', result_map.get(item[0]))
        if result_map.get(item[0]) is not None:
            result_map[item[0]] = result_map.get(item[0]) + item[1]
        else:
            result_map[item[0]] = item[1]
            
    return result_map


print('Summation of dict: ', summationOfMap(tuples_list))
        

## Dictionary comprehension with words len in list

words_list = ["wordfgdfgd1", "wfford2", "word3"]
new_map = {word_item:len(word_item) for (word_item) in words_list}

print('new dict comprehension', new_map)






