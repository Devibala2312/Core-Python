tuple1 = (1, 2, 3, 4)
tuple2 = (4, 5, 6, 2)

combined = tuple(set(tuple1).union(tuple2))

print(combined)

