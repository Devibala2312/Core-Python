# 17. Write a program that finds the sum of all even numbers from 1 to 100 using a for loop

def sum_of_even():
    total = 0
    for num in range(1, 101):
        if num % 2 == 0:
            total = total + num

    return total

print(sum_of_even())