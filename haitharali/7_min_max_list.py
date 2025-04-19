# 7. Given a list of integers, find the largest and smallest
# numbers in the list without using the built-in max() and min() functions

def min_max_list(input_list):
    length = len(input_list)
    if length == 0:
        print("List is Empty")
    else:
        for i in range(length):
            for j in range(i + 1, length):
                if input_list[i] > input_list[j]:
                    x = input_list[i]
                    input_list[i] = input_list[j]
                    input_list[j] = x
        print("input list", input_list)
        print("minimum is ", input_list[0])
        print("maximum is ", input_list[-1])


min_max_list([4, 3, 5, 1, 2])
min_max_list([])
