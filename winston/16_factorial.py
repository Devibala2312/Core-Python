def factorial(input_num):

    output = 1
    i = 1

    while i <= input_num:
        output *= i
        # print(f'Output: {output}')
        i += 1
        # print(f'i: {i}')
    return output

num = 4
print(f"Factorial of the given number: {num} is {factorial(num)}")