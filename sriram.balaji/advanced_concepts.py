# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 09:22:55 2025

@author: sriram.balaji
"""

###Scopes Global vs local pagevisit

visits = 0

def track_visit(page):
    global visits  
    visits += 1
    message = f"User visited {page}. Total visits: {visits}"  # Local variable
    print(message)


track_visit("Homepage")
track_visit("Homepage")
track_visit("About Us")
track_visit("Contact")
print(visits)



##Built-in functions in python

from functools import reduce

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [85, 42, 73, 60, 29]

zipped_results = zip(names, scores)
list_of_zipped_results = list(zipped_results)
print('Paired values : ', list_of_zipped_results)
print('Type of Paired values : ', type(zipped_results))

def map_function(x: tuple):
    y = ''
    if x[1] >= 85:
        y = "A"
    elif x[1] < 84 and x[1] >= 70:
        y = "B"
    elif x[1] < 69 and x[1] >= 50:
        y = "C"
    else:
        y = "F"

    return (x[0], x[1], y)


def reduce_function(x: int, y: int):
    return x + y

mapped_result = map(map_function, list_of_zipped_results)
list_of_mapped_result = list(mapped_result)

filterd_result = filter(lambda x: x[2] not in ['F'], list_of_mapped_result)
print('Mapped result : ', list_of_mapped_result)
print('Filtered result : ', list(filterd_result))

# reduced_result = reduce(lambda x, y: x + y, list_of_mapped_result)
reduced_result = reduce(reduce_function, scores)
print('Total Score : ', str(reduced_result))



for index, value in enumerate(list_of_mapped_result, start=1):
    print('Index : ', index, 'Student : ', value[0])



