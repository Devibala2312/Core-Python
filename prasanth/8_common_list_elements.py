list1=input("Enter the first list elements(separated by comma): ")
list1=[item.strip() for item in list1.split(",")]
list2=input("Enter the second list elements(separated by comma): ")
list2=[item.strip() for item in list2.split(",")]
common_elements = []
for ele in list1:
    if ele in list2:
        common_elements.append(ele)

print("The common elements are: ", common_elements)