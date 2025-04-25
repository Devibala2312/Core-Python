# 21. Write a program to yield positive number from the given listing using python generator

def positive_numbers(numbers):
    for num in numbers:
        if num > 0:
            yield num
            
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positive_nums = positive_numbers(numbers)
print(list(positive_nums))




