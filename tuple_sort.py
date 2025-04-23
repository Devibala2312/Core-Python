def sort_by_last_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])

# Example usage:
sample_list = [(9, 5), (9, 2), (8, 4), (8, 3), (8, 1)]
sorted_list = sort_by_last_element(sample_list)
print("Sorted list:", sorted_list)
