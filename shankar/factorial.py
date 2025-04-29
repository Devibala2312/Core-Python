def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Example usage
number = 5
print(f"Factorial of {number} is {factorial(number)}")
