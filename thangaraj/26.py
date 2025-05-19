from functools import reduce

names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [85, 42, 73, 60, 29]

paired_data = list(zip(names, scores))
print(paired_data)

def convert_to_grade(score):
    if score >= 85:
        return 'A'  
    elif score >= 70:
        return 'B'
    elif score >= 50:
        return 'C'
    else:
        return 'F'  

letter_grades = list(map(convert_to_grade, scores))
print(letter_grades)

passed_students = list(filter(lambda x: x[1] >= 50, paired_data))
print(passed_students)  


total_score = reduce(lambda x, y: x + y[1], paired_data, 0)
print(total_score)

for index, student in enumerate(names, 1):
    print(f"{index}. {student}")

print(type(paired_data))    

print(id(scores))

for rank in range(1, len(names) + 1):
    print(rank)



