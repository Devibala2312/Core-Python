def double_values(tuple_list):
    return tuple(x*2 for x in tuple_list)

word_tuple = input("Enter the inputNumbers in tuple separated by comma: ")
items = tuple(int(word.strip()) for word in word_tuple.split(","))
print("Scores aggregated by name: ", double_values(items))