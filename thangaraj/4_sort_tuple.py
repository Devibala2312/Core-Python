sampleList = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1), (2,7,6), (1,2,0)]

sampleList.sort(key=lambda item: item[len(item) - 1])

print(sampleList)

