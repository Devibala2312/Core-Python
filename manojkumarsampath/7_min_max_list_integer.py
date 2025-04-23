#7. Given a list of integers, find the largest and smallest numbers in the list
# without using the built-in max() and min() functions.

def find_min_max(numbers):
    if not numbers:
        return None, None  # Handle empty list

    smallest = largest = numbers[0]

    for num in numbers[1:]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest

# Example usage
sample_list = [5, 3, 8, 6, 2, 10, 4]
min_val, max_val = find_min_max(sample_list)
print("Smallest:", min_val)
print("Largest:", max_val)
