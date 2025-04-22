def sum_of_scores(scores):
    scores_dict = {}
    for name,score in scores:
        if name in scores_dict:
            scores_dict[name]+=score
        else:
            scores_dict[name] = score
    return scores_dict

print(sum_of_scores( [('Alice', 90), ('Bob', 85), ('Alice', 95)]))