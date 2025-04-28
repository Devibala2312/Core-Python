# 21. Write a program to yield positive
# number from the given listing using python generator

def positive_numbers(numbers):
    for num in numbers:
        if num > 0:
            yield num

# Example list
my_list = [-3, -2, 0, 1, 2, 4, 5, 7]

# Using the generator
print("Positive numbers are:")
for number in positive_numbers(my_list):
    print(number)