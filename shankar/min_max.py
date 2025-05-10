numbers = [23, 1, 45, -10, 77, 5]

largest = max(numbers)
smallest = min(numbers)

print("Largest:", largest)
print("Smallest:", smallest)


numbers = [23, 1, 45, -10, 77, 5]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)
