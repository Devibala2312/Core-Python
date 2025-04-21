#find the largest and smallest number in a list

def find_largest_number(x): 
    largest = x[0]

    for y in range(1, len(x)):
        if x[y] > largest:
            largest = x[y]

    return largest

def find_smallest_number(x):
    smallest = x[0]

    for z in range(1, len(x)):
        if x[z] < smallest:
            smallest = x[z]

    return smallest

print(find_largest_number([21, 22, 9, 1, -1]))
print(find_smallest_number([21, 22, 9, 1, -1]))


