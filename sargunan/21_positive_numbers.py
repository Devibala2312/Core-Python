# 21. Write a program to yield positive number from the given listing using python generator

def positive_numbers(numbers):
    for num in numbers:
        if num > 0:
            yield num


numbers_list = [-5, 3, -1, 7, 0, -2, 8]
positive_list = list(positive_numbers(numbers_list))
print(positive_list)