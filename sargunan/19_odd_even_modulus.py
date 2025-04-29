# 19. Write a program that takes a number and determines if it's even or odd using the modulus operator %

def odd_or_even(num):
    if num % 2 == 0:
        print('given number is even')
    else:
        print('given number is odd')

number = int(input('Enter a number'))
odd_or_even(number)