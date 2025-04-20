#2.Write a Python program to filter and count strings that have more than 2 characters and the first and last characters are the same.
ip = ['abc', '121','madam', '242', 'pop', 'mam', 'oo']
count = 0
for i in ip:
    if len(i) > 2 and i[0] == i[-1]:
        print(i)
        count += 1

print(f'The number of strings that have more than 2 characters and the first and last characters are the same is: {count}')

