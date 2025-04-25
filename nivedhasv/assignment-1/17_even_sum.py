# 17. Write a program that finds the sum of all even numbers from 1 to 100 using a for loop

def sum_even_numbers(num):
    sum = 0
    for i in range(1,num+1):
        if i%2 == 0:
            sum += i
    return sum

print(sum_even_numbers(100))



