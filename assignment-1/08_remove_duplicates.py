#remove duplicates from two lists

def remove_duplicates(list1, list2 ):
    list3 = []
    for x in list1:
        if x not in list2:
            list3.append(x)
    return set(list3)

print(remove_duplicates([1, 2, 3, 4, 5], [3, 2, 1, 9, 8]))
