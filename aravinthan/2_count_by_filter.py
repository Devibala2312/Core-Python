# Method 1 
input = ['abc', 'xyz', 'aba', '1221']
min_lambda = lambda x: len(x) > 2
char_match_lamda = lambda x: x[0] == x[-1]
result = filter(min_lambda, input)
result = filter(char_match_lamda, result)
print(len(list(result)))

# Method 2
result = [x for x in input if len(x) > 2 and x[0] == x[-1]]
print(len(result))