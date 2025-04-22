# 21. Write a program to yield positive number from the given listing using python generator

def positive_counter(num_list):
    for num in num_list:
        if num >=0:
            yield num

get_positive_num = positive_counter([1,2,3,4,-1,-5,6,0,-7,8])
for value in get_positive_num:
    print(value)