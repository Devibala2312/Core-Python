# 26. Builtin functions
# You are given two lists:
# A list of student names
# A list of scores they received in a test.
from functools import reduce

student_names = ["Alice" , "Bob" , "Charlie", "Diana" , "Eve"]
student_scores = [85,42,73,60,29]

# 1.Pair the names with scores using zip().
pair_names_scores = list(zip(student_names,student_scores))
print("Paired data(zip): ",pair_names_scores)

# 2. Use map() to convert the scores into letter grades:
# 85 and above: 'A'
# 70–84: 'B'
# 50–69: 'C'
# Below 50: 'F'

def condition_check(score):
    if score >=85:
        return 'A'
    elif score >=70:
        return 'B'
    elif score>=50:
        return 'C'
    else:
        return 'F'

student_grades = list(map(condition_check,student_scores))
print("Grades (map): ",student_grades)

# 3.Use filter() to get only the students who passed (score ≥ 50).
pass_students = list(filter(lambda student: student[1]>50,pair_names_scores))
print("Students who passed(filter): ", pass_students)

# 4.Use reduce() to calculate the total score.
total_score = reduce(lambda score1,score2:score1+score2,student_scores)
print("Total scores(reduce): ", total_score)

# 5.Use enumerate() to print each student with their index (starting from 1).
student_index = enumerate(student_names)
print("Student list with index(enumerate):")
for index,name in enumerate(student_names):
    print(f"{index+1}:{name}")

# 6.Use type() to print the type of the paired data.
type_of_paired = type(pair_names_scores)
print("Type of 'paired': ", type_of_paired)

# 7.Use id() to print the memory address of the scores list.
id_of_scores = id(student_scores)
print("ID of scores list:  ", id_of_scores)

# 8.Use range() to generate and print ranks from 1 to number of students.
rank_students = list(range(1, len(student_scores)+1))
print("Ranks(range): ",rank_students)
