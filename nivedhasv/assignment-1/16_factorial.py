# 16. Write a program to find the factorial of a number using a while loop.

def find_factorial(num):
    op = 1
    while num > 1:
       op *= num
       num -= 1
    print(op)
    
find_factorial(3)
find_factorial(5)
find_factorial(10)
        

