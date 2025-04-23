# Write a Python program to get a list, sorted in increasing order by the last element in
# each tuple from a given list of non-empty tuples. Go to the editor

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
sorted_list = sorted(sample_list, key=lambda x: x[-1])

print("Sorted List by last element: ", sorted_list)