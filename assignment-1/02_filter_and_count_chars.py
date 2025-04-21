# count strings that have more than 2 characters and the first and last characters are the same.

def count_strings(list_of_strings):
    count = 0
    for x in list_of_strings:
        if len(x) >=2 and x[0] == x[-1]:
            count += 1
    return count

print(count_strings(['abc', 'xyz', 'aba', '1221']))
