def set_of_list(input1, input2):
    return set(input1).intersection(set(input2))
    
    
input1 = [0,1,2]
input2 = [1,2,3]
print(set_of_list(input1,input2))