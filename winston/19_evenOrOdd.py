# Write a program that takes a number and determines if it's even or odd using the modulus operator %

def check_if_even_or_odd(input):
    if input % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print('The given number is: ', check_if_even_or_odd(45))