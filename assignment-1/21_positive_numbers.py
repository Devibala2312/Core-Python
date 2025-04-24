# positive numbers

def positive_numbers(numbers):
    for num in numbers:
        if num > 0:
            yield num

nums = [-3, -2, 0, 1, 2, 4, 5, 7]

for number in positive_numbers(nums):
    print(number)
