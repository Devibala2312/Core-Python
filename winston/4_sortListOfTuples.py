
def sortListOfTuples(inputList, sortApproach):
    return (sorted(inputList, key = lambda i: i[sortApproach]))

print('Sorting by last element:', sortListOfTuples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)], 1))

print('Sorting by first element:', sortListOfTuples([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)], 0))