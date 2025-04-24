firstList = [1, 3, 4, 5, 7, 7, 3]
secondList = [2, 3, 5, 6, 9]



commonItems = {item for item in firstList if item in secondList}

print(commonItems)

