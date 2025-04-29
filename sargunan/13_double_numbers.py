# 13. Write a function that takes a tuple of numbers and returns a new tuple with each element doubled

def double_numbers(nums):
    return tuple(num * 2 for num in nums)

numbers = (1,2,3,4,5)
result = double_numbers(numbers)
print(result)