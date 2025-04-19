# 8. Write a function that takes two lists and returns a set of elements that are common to both lists.

def common_elements_in_lists(list1, list2):
    outputlist = []
    print("input list 1", list1)
    print("input list 2", list2)
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                outputlist.append(list1[i])
    print("common value list ", outputlist)


common_elements_in_lists([1, 2, 3], [5, 1, 3])
common_elements_in_lists([6, 4, 3], [5, 1, 3, 4, 6, 7])
