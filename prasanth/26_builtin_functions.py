from functools import reduce

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [85, 42, 73, 60, 29]

#1. Pair names with score using zip
paired = list(zip(names, scores))
print("Paired data: ", paired)

#2. Convert scores into letter grade
def get_grades(score):
    if score >= 85:
        return "A"
    elif 70<= score <= 84:
        return "B"
    elif 50<= score <=69:
        return "C"
    else:
        return "F"

grades = list(map(get_grades, scores))
print("Grades: ", grades)

#3. Get passed students list
def check_passed(detail):
    name, score = detail
    return score >= 50
passed_students = list(filter(check_passed, paired))
print("Passed students: ", passed_students)

#4. Use reduce() to calculate the total score
total = reduce(lambda x,y: x+y, scores)
print("The total score is: ", total)

#5. enumerate()
print("Student list with index (enumerate):")
for index, name in enumerate(names, start = 1):
    print(f"{index}. {name}")

#6. Type of paired list
print("Type of 'paired': ", type(paired))

#7. Memory of scores list
print("ID of scores list: ", id(scores))

#8. range()
ranks = list(range(1, len(names) + 1))
print("Ranks (range):", ranks)