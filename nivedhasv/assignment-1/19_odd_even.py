#19. Write a program that takes a number and determines if it's even or odd using the modulus operator %

def check_odd_even(num):
    if num%2 == 0:
        print("even")
    else:
        print("odd")
        
check_odd_even(2)
check_odd_even(3)
