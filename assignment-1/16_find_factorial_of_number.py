#  find the factorial of a numbe

def find_factorial(num):
    factorial = 1
    n = num
    while n > 1:
        factorial *= n
        n -= 1
    return factorial

result = find_factorial(5)
print(f"Factorial of 5 is {result}")
