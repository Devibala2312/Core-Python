#4 .Write a Python program to get a list, sorted in increasing order by
# the last element in each tuple from a given list of non-empty tuples.
# Go to the editor

def sort_by_last_element(sample_list):
    return sorted(sample_list, key=lambda x: x[-1])

# Sample input
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Function call and output
sorted_list = sort_by_last_element(sample_list)
print(sorted_list)
