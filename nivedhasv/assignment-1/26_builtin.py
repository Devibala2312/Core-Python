
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [85, 42, 73, 60, 29]

# 1. Pair the names with scores using zip()
paired = list(zip(names, scores))
print("Paired names and scores:", paired)

# 2. Use map() to convert the scores into letter grades
def convert_to_grade(score):    
    if score >= 85:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 50:
        return 'C'
    else:
        return 'F'
grades = map(convert_to_grade, scores)

for name, grade in zip(names, grades):
    print(f"{name}: {grade}")

# 3. Use filter() to get only the students who passed (score ≥ 50)
passed_students = filter(lambda x: x[1] >= 50, paired)
print("Passed students:", list(passed_students))

# 4. Use reduce() to calculate the total score
from functools import reduce
total_score = reduce(lambda x, y: x + y[1], paired, 0)
print("Total score:", total_score)

# 5. Use enumerate() to print each student with their index (starting from 1)
for index, (name, score) in enumerate(paired, start=1):
    print(f"Student {index}: {name} with score {score}")

# 6. Use type() to print the type of the paired data
print("Type of paired data:", type(paired))

# 7. Use id() to print the memory address of the scores list
print("Memory address of scores list:", id(scores))

# 8. Use range() to generate and print ranks from 1 to number of students
ranks = range(1, len(names) + 1)
print("Ranks:", list(ranks))


