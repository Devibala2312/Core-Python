def set_of_list(ip1,ip2):
    return set(ip1).intersection(set(ip2))
    
    
ip1 = [3,4,1]
ip2 = [1,4,5]
print(set_of_list(ip1,ip2))