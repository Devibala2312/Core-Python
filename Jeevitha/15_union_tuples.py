def merge_tuple(tuple1,tuple2):
    return tuple(set(tuple1+tuple2))

input1 = ("orange","banana","banana","grape")
input2 = ("apple","banana","watermelon","grape")
print(merge_tuple(input1, input2))