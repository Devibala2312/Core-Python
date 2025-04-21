# sum of scores of students

def sum_of_scores(x):
    dict_of_students_scores = {}
    for a,b in x:
        if a in dict_of_students_scores:
            dict_of_students_scores[a] += b
        else:
            dict_of_students_scores[a] = b
    return dict_of_students_scores

print(sum_of_scores([('Alice', 90), ('Bob', 85), ('Alice', 95)]))
