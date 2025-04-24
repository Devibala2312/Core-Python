# find the sum of all even numbers from 1 to 100

def sum_of_even_numbers():
    sum = 0
    for i in range(1, 101):
        if i % 2 == 0:
            sum += i
    return sum

result = sum_of_even_numbers()
print(f"Sum of all even numbers from 1 to 100 is {result}")

