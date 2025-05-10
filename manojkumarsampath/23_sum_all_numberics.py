# 23. Write a function sum_all(*args) that accepts
# any number of numeric arguments and returns their sum.

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_all(1, 2, 3)
print(f"The sum is: {result}")