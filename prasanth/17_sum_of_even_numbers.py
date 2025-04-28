def get_even_nums_sum():
    total = sum(x for x in range(1, 101) if x % 2 == 0)
    return total

print("The sum of even numbers between 1 to 100 is: ", get_even_nums_sum())
