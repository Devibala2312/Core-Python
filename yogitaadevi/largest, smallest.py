def find_largest_smallest(numbers):
    if not numbers:
        return None, None
    largest = smallest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest

nums = list(map(int, input("Enter numbers: ").split()))
largest, smallest = find_largest_smallest(nums)
print(largest)
print(smallest)
