input = ['abcd', '1211','madam', '77', '0']
count = 0
for i in input:
    if len(i) >= 2 and i[0] == i[-1]:
        print(i)
        count += 1

print(f'The number of strings that have equals to or more than 2 characters and the first and last characters are the same is: {count}')