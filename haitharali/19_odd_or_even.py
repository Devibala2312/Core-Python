# 19. Write a program that takes a number and determines if it's even or odd using the modulus operator

def odd_or_even(number):
    output = 'even' if number%2 == 0 else 'odd'
    return f"number is {output}"

print(odd_or_even(5))
print(odd_or_even(6))