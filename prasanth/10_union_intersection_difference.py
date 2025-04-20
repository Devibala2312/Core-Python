list1=input("Enter the first list elements(separated by comma): ")
list1=[item.strip() for item in list1.split(",")]
list2=input("Enter the second list elements(separated by comma): ")
list2=[item.strip() for item in list2.split(",")]

print("Union of two list: ", list(set(list1) | set(list2)))
print("Intersection of two list:", list(set(list1) & set(list2)))
print("Difference of two list:", list(set(list1) - set(list2)) + list(set(list2) - set(list1)))