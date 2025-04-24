# Write a function sum_all(*args) that accepts any number of numeric arguments and returns their sum.

def sum_all_numeric_args(*args):
    return sum(args)

print('The sum of all numeric args: ', sum_all_numeric_args(1, 2, 3))

print('The sum of all numeric args: ', sum_all_numeric_args(2, 5, 8.5, 9, 0.3, 11))

print('The sum of all numeric args: ', sum_all_numeric_args(9, 5.5))

print('The sum of all numeric args: ', sum_all_numeric_args(3))

print('The sum of all numeric args: ', sum_all_numeric_args())