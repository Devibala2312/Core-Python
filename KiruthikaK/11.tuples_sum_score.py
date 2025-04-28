def sum_scores_by_name(scores):
    dict1={}
    for k,v in scores:
        dict1[k] = v if k not in dict1 else (dict1[k]+v)
    return dict1

scores = [('Alice', 90), ('Bob', 85), ('Alice', 95)]
print(sum_scores_by_name(scores))
