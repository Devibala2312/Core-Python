# Given a list of tuples where each tuple contains a name and a score (e.g., [('Alice', 90), ('Bob', 85), ('Alice', 95)]), write a function to return a dictionary where each name maps to the sum of their scores.

tuplesList = [('Alice', 50), ('Bob', 65), ('Alice', 95)]

targetDictionary = {}

def create_dict(input_list):
    for name, score in input_list:
        if name in targetDictionary:
            targetDictionary[name] += score
        else:
            targetDictionary[name] = score
    return targetDictionary

print('Final output: ', create_dict(tuplesList))