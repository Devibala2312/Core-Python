#check if two tuples are equal

def check_tuples_are_equal(tuple1, tuple2):
    if tuple1 == tuple2:
        return True
    else:
        return False
    
print(check_tuples_are_equal((1, 2, 3), (3, 2, 1)))
