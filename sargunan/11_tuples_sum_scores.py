# Given a list of tuples where each tuple contains a name and a score (e.g., [('Alice', 90), ('Bob', 85), ('Alice', 95)]),
# write a function to return a dictionary where each name maps to the sum of their scores.

def sum_scores(dict_names):
    output = {}
    for name, score in dict_names:
        if name in output:
            output[name] += score
        else:
            output[name] = score
    return output

input_list = [('Alice', 90), ('Bob', 85), ('Alice', 95), ('Bob', 15)]
result = sum_scores(input_list)
print(result)