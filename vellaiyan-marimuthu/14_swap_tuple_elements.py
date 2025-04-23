def swap_values(tuple_list):
    return (tuple_list[-1],) + tuple_list[1:-1] + (tuple_list[0],)

number_tuple = input("Enter the numbers in tuple separated by comma: ")
items = tuple(int(word.strip()) for word in number_tuple.split(","))
print("Modified tuple: ", swap_values(items))