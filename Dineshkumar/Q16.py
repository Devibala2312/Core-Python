#16. Write a program to find the factorial of a number using a while loop.

num = int(input("Enter a number: "))

factorial = 1

value = 1
while value <= num:
    factorial *= value
    value += 1

print(f"The factorial of {num} is {factorial}")
