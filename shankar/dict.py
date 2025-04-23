from collections import defaultdict


def sum_of_score(input_string):
    sum_value = defaultdict(int)
    for name, score in input_string:
        sum_value[name] += score
    return dict(sum_value)

data = [('Alice',80),('Bob',90),('Alice',100)]
print(sum_of_score(data))