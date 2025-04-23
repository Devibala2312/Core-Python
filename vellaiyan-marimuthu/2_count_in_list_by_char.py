print("Program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.")
list = input("Enter the items separated by comma: ")
items = [word.strip() for word in list.split(",")]
filteredItem = [item for item in items if len(item)>=2 and item[0] == item[-1]]

print("Words matching the criteria", filteredItem)
print("Count", len(filteredItem))