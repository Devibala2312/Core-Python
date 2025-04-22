input = [90,5,1,0,100,-1]

if len(input) == 0:
    print('List is empty')
else:
    min = input[0]
    max = input[0]
    for x in input:
        if min > x:
            min = x
        if max < x:
            max = x
print(f'Minimum value in the list is: {min}')
print(f'Maximum value in the list is: {max}')