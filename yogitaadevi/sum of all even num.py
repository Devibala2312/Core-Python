def sum_of_even_numbers(n):
    sum = 0
    for i in range(0,n):
        if i % 2 == 0:
            sum += i
    return sum
num = 100;
print(sum_of_even_numbers(num))