from functools import reduce

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [85, 42, 73, 60, 29]

# ZIP
concat_result = zip(names, scores)
for i in concat_result:
    print(i)
    
# MAP
def changeToGrades(score):
    if score >= 85 :
        return "A"
    elif score < 85 and score > 70:
        return "B"
    elif score < 69 and score > 50:
        return "C"
    else:
        return "F"
    
result = map(changeToGrades, scores)

print(list(result))

# Filter
def isPassed(score):
    return score[1] >= 50

passed_students = filter(isPassed, concat_result)

print(list(passed_students))

# Reduce
def findTotalScore(a, b):
    return a + b
reduce(findTotalScore, scores)

# Enumeration
for i, name in enumerate(names):
    print(f"{i+1}. {name}")
    
# Type
print(type(concat_result))

# Memory Address
print(id(concat_result))

# Ranks
ranks = [ x for x in range(1, len(names)+1) ]
print(ranks)