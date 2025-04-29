# 16. Write a program to find the factorial of a number using a while loop.

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

num = 5
print(factorial(num))