def find_largest_smallest(numbers):
    large_num = small_num = numbers[0]

    for num in numbers[1:]:
        if num > large_num:
            large_num = num

        if num < small_num:
            small_num = num

    return large_num, small_num

nums = [12, 5, 7, 34, 2, 99, 21]
largest, smallest = find_largest_smallest(nums)

print("Largest number:", largest)
print("Smallest number:", smallest)