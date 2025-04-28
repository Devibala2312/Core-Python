sample_list = ['abc', 'xyz', 'aba', '1221']
count = sum(1 for word in sample_list if len(word) >= 2 and word[0] == word[-1])
print(count)