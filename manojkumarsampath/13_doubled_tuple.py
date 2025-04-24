# 13. Write a function that takes a tuple of numbers and
# returns a new tuple with each element doubled

def double_elements(numbers):
    return tuple(x * 2 for x in numbers)

original = (1, 2, 3, 4)
doubled = double_elements(original)
print(doubled)
