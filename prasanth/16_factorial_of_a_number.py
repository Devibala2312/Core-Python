def get_factorial_value(num):
    value = 1
    while num>0:
        value *= num
        num -= 1
    return value

factNumber = int(input("Enter the number to get factorial value: "))
print("The factorial value is ", get_factorial_value(factNumber))