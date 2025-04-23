def unique_records_list(list1,list2):
    return set(list1) & set(list2)

def another_unique_records_list(list1,list2):
    return list(set(list1).intersection( set(list2)))

print(unique_records_list([1,2,3,4,5,6,7,8,9],[1,2,7,8,9]))
print(another_unique_records_list([1,2,3,4,5,6,7,8,9],[1,2,7,8,9]))