list1 = [1, 45, 2, 100, 3]
list2 = [4, 3, 5, 1, 6, 99]

target_set = set()
target_set.update(list1)

for i in list2:
    if i not in target_set:
        target_set.add(i)

print(target_set)