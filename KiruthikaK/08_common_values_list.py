

def common_elements(list1, list2):
    return set(list1) & set(list2)
list1 = [int(1), 2, None,3, 4, 5,'A']
list2 = [4, 5, None,bool(True),6, 7, 8,"A"]
print(common_elements(list1, list2))