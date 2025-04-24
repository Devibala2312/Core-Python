# 6. Create a list comprehension that generates a list of squares of inputNumbers from 1 to 20.

def squares_of_list(value):
    comprehension_list = [x * x for x in range(1, value + 1)]
    print(f"comprehension list of squares till {value} is {comprehension_list}")


squares_of_list(20)
