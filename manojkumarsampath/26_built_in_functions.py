from functools import reduce

# Input data
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [85, 42, 73, 60, 29]

# 1. Paired data using zip
paired = list(zip(names, scores))
print("Paired data (zip):", paired)

# 2. Use map() to convert the scores into grades
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
print("Grades (map):", grades)

# 3. Use filter() to get only the students who passed score ≥ 50
passed = list(filter(lambda pair: pair[1] >= 50, paired))
print("Students who passed (filter):", passed)

# 4. Use reduce() to calculate the total score
total_score = reduce(lambda x, y: x + y, scores)
print("Total score (reduce):", total_score)

# 5. Use enumerate()
print("Student list with index (enumerate)")
for index, name in enumerate(names, start=1):
    print(f"  {index}. {name}")

# 6. Use type() to print the type of the paired data
print("Type of 'paired':", type(paired))

# 7. Use id() to print the memory address
print("ID of scores list:", id(scores))

# 8. Use range() to generate and print ranks from 1 to number of students
ranks = list(range(1, len(names) + 1))
print("Ranks (range):", ranks)
