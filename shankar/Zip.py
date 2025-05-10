from functools import reduce

# 1. Pair the names with scores using zip()
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [85, 42, 73, 60, 29]
paired_data = list(zip(names, scores))
print("1. Paired Data (name, score):", paired_data)
name,score=list(zip(*paired_data))
print("2. Name:", list(name))
print("3. score:", score)

# 2. Use map() to convert the scores into letter grades
def get_grade(score):
    if score >= 85:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 50:
        return 'C'
    else:
        return 'F'

grades = list(map(get_grade, scores))
print(map(get_grade, scores));
print(tuple(map(get_grade, scores)));
print("2. Grades:", grades)

# 3. Use filter() to get only the students who passed (score ≥ 50)
passed = list(filter(lambda x: x[1] >= 50, paired_data))
print("3. Passed Students (name, score):", passed)

# 4. Use reduce() to calculate the total score
total_score = reduce(lambda acc, x: acc + x, scores)
print("4. Total Score:", total_score)

# 5. Use enumerate() to print each student with their index (starting from 1)
print("5. Students with Index:")
for index, name in enumerate(names, start=1):
    print(f"   {index}. {name}")

# 6. Use type() to print the type of the paired data
print("6. Type of paired_data:", type(paired_data))

# 7. Use id() to print the memory address of the scores list
print("7. Memory address of scores list:", id(scores))

# 8. Use range() to generate and print ranks from 1 to number of students
ranks = list(range(1, len(names) + 1))
print("8. Ranks:", ranks)
