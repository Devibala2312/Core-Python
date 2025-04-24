def find_common_elements(list1, list2):
    return set(list1).intersection(list2);

list1 = list(map(int, input("Enter list: ").split()))
list2 = list(map(int, input("Enter list: ").split()))
print(find_common_elements(list1, list2))