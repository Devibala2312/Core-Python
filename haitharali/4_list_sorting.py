# 4 .Write a Python program to get a list, sorted in increasing order by the last element
# in each tuple from a given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def sorted_list(my_list):
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i][1] > my_list[j][1]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    print(my_list)


sorted_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
