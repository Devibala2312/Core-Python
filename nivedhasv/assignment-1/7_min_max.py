ip = [3,4,2,6,1]

if len(ip) == 0:
    print('List is empty')
else:
    min = ip[0]
    max = ip[0]
    for val in ip:
        if min > val:
            min = val
        if max < val:
            max = val
print(f'Minimum value in the list is: {min}')
print(f'Maximum value in the list is: {max}')