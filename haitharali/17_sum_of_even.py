def sum_of_even(number):
    sum_value = 0
    for n in range(1, number + 1):
        if n % 2 == 0:
            sum_value = sum_value + n
            n -= 1
    print(f"sum of even from 1 till {number} is {sum_value}")


sum_of_even(100)
