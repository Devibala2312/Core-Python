# 11. Given a list of tuples where each tuple contains a name and a score (e.g., [('Alice', 90), ('Bob', 85), ('Alice', 95)]), write a function to
# return a dictionary where each name maps to the sum of their scores.

def sum_scores(tuples_list):
    score_dict = {}
    for name, score in tuples_list:
        if name in score_dict:
            score_dict[name] += score
        else:
            score_dict[name] = score
    return score_dict

score_list = [('Alice', 90), ('Bob', 85), ('Alice', 95), ('Bob', 10)]
print("Individual scores", sum_scores(score_list))
