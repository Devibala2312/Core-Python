def sum_even_numbers():
    total = 0
    for number in range(1, 101):
        if number % 2 == 0:
            total += number
    return total

print(sum_even_numbers())