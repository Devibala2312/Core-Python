def sum_scores_by_name(tuple_list):
    name_score={}
    for name,score in tuple_list:
        if name in name_score:
            name_score[name] += score
        else:
            name_score[name] = score

    return name_score

score_tuple = [('Alice', 90), ('Bob', 85), ('Alice', 95)]
print("Scores aggregated by name: ", sum_scores_by_name(score_tuple))