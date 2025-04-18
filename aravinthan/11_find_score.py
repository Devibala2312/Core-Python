input = [('Alice', 90), ('Bob', 85), ('Alice', 95)]
def calculateScore(input):
    result = {}
    for i in input:
        result[i[0]] = result.get(i[0],0) + i[1]
    return result
print(calculateScore(input))