# 15. Write a function that takes two tuples and returns a new tuple that contains all elements from both tuples without any duplicates.

def merge_tuple(tuple1,tuple2):
    return tuple(set(tuple1+tuple2))

ip1 = ("apple","banana","apple","orange","banana","grape")
ip2 = ("apple","banana","apple","orange","watermelon","grape")
print(merge_tuple(ip1,ip2))



