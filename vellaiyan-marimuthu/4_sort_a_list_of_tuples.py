print("Program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.")

unsortedTupleList = [(2,2,1), (1,2,3), (1,2,0), (1,2,1), (1,2,5), (1,2,4), (2,1,5)]
unsortedTupleList.sort(key=lambda x: x[-1])
print("The sorted list is: ", unsortedTupleList)
