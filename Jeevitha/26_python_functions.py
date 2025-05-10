from functools import reduce
from tkinter.font import names


def score_to_grade(score):
    if score >= 85:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 50:
        return 'C'
    else:
        return 'F'

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [85, 42, 73, 60, 29]

paired_data = list(zip(names,scores))
print('Paired data (zip):',paired_data)

grades = list(map(score_to_grade,scores))
print('Grades (map):',grades)

passed_students = list(filter(lambda student: student[1] >= 50, paired_data))
print('Students who passed (filter):',passed_students)

total_score = reduce(lambda x,y:x+y,scores)
print('Total score (reduce):',total_score)

for i,val in enumerate(names,start=1):
    print(i,val)

print("Type of 'paired':",type(paired_data))
print('ID of scores list:',id(scores))

ranks = list(range(1,len(names)+1))
print('Ranks (range):',ranks)