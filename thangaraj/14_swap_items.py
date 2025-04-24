testTuple = (1, 2, 3, 4, 5)

swapped = tuple([testTuple[-1], *testTuple[1:-1], testTuple[0]])

print(swapped)


