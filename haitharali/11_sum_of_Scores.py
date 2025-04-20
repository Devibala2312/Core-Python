# 11. Given a list of tuples where each tuple contains a name and a score
# (e.g., [('Alice', 90), ('Bob', 85), ('Alice', 95)]),
# write a function to return a dictionary where each name maps to the sum of their scores.

def sum_of_scores(player_score):
    individual_scores = {}
    for player, score in player_score:
        if player in individual_scores:
            individual_scores[player] += score
        else:
            individual_scores[player] = score

    print("individual scores of each person ", individual_scores)


player_scores = [('Alice', 90), ('Bob', 85), ('Alice', 95)]
sum_of_scores(player_scores)
