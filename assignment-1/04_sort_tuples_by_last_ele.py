# sort a list of tuples by the last element of each tuple

def sort_by_last_element(tuples):
    return sorted(tuples, key = lambda x: x[-1])

print(sort_by_last_element([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
