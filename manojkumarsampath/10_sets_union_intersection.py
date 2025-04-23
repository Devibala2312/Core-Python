#10. Given two sets, write a function to return
# their union, intersection, and difference.

def set_operations(set1, set2):
    union = set1 | set2
    intersection = set1 & set2
    difference = set1 - set2
    return union, intersection, difference

# Example usage
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

union, intersection, difference = set_operations(set_a, set_b)

print("Union:", union)
print("Inter :", intersection)
print("Diff :", difference)