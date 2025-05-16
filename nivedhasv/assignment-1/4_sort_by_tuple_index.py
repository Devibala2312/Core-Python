# 4 .Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor

ip = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# using lambda function
print(f'Using Lambda Function: {sorted(ip, key=lambda item: item[1])}')


# using named function
def keyfn(tpip):
    return tpip[1]
    
print(f'Using Named Function: {sorted(ip,key=keyfn)}')