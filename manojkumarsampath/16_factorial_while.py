# 16. Write a program to find the factorial of a number using a while loop.

# Input from the user
num = 5

# Initialize variables
factorial = 1
i = 1

# Check if the number is negative, positive, or zero
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    while i <= num:
        factorial *= i
        i += 1
    print(f"The factorial of {num} is {factorial}.")