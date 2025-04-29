#14. Write a function that swaps the first and last elements of a tuple.
itemList = (49,88,9,0,5)
newList = list(itemList)
numbe = newList[0]
newList[0]= newList[-1]
newList[-1]= numbe

print(tuple(newList))

# def swapplist(itemList):
#     if len(itemList) < 1:
#         return iteamList
#     else:
#         return ((itemList[-1],)+ (itemList[1:-1],)+ (itemList[0],))
# itemList2 = (49,88,9,0,5)
# print(swapplist(itemList2))