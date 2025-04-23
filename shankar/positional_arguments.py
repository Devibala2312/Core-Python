def sum_positional_arguments(*args):
    final_sum = 0
    for value in args:
        if isinstance(value, int):
            final_sum +=  value
        else:
            print(f"String can not sum{value}")
    return final_sum
print(sum_positional_arguments(1,2,3,'test'))