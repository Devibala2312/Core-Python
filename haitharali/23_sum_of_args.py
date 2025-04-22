# 23. Write a function sum_all(*args) that accepts any number of numeric arguments
# and returns their sum.

def sum_of_arguments(*args):
    return sum(args)

print(sum_of_arguments(1,2,3,4,7))