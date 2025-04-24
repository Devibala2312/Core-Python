# 7. Given a list of integers, find the largest and smallest numbers in the list without using the built-in max() and min() functions.

list_of_integers = [7, 2, 3, 4, 11, 6, 1, 8, 9]
max_value = list_of_integers[0]
min_value = list_of_integers[0]
for number in list_of_integers:
    if number < min_value:
        min_value = number
    if number > max_value:
        max_value = number
print("Smallest number is", min_value)
print("Largest number is", max_value)