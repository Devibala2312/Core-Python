# 16. Write a program to find the factorial of a number using a while loop.

def calculate_factorial(number):
    factorial = 1
    n = number
    while n > 1:
        factorial = factorial * n
        n -= 1
    print(f"factorial for number {number} is {factorial}")


calculate_factorial(5)
calculate_factorial(10)
