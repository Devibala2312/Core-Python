rollNos = [5, 11, 6, 199, 1, 45]

var = 0

outputDict = {}

for x in rollNos:
    if x > var:
        var = x

outputDict['max'] = var

for y in rollNos:
    if y < var:
        var = y

outputDict['min'] = var

print(outputDict)