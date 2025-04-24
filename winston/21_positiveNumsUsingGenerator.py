def positive_numbers(input_numbers):
    for num in input_numbers:
        if num > 0:
            yield num
            # print(num)
        else:
            print(f'{num} is not a positive number')

nums = [-3, -2, 0, 1, 2, 4, 5, 7]

for positive in positive_numbers(nums):
    print('Positive number: ', positive)