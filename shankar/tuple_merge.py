tuple1=(1,2,3,4,5,6,7,8,9)
tuple2=(1,2,3,7,8,9)
def remove_and_merge(tuple1, tuple2):
    return tuple(set(tuple1+tuple2))
print(remove_and_merge(tuple1, tuple2))