def even_odd_check(num):
    return 'event' if num % 2 == 0 else 'odd'

input_num = int(input("Input the number to check: "))
print("The given number is ", even_odd_check(input_num))