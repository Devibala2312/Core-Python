def get_totalSum(tuple):
    result_dict = {}
    for name, score in tuple:
        if name in result_dict:
            result_dict[name] += score
        else:
            result_dict[name] = score
    return result_dict

list_of_tuples = []
num = int(input("Enter a number of tuple: "))
for _ in range(num):
    name, score = input("Enter a name and score: ").split()
    list_of_tuples.append((name, int(score)))
print(get_totalSum(list_of_tuples))
