def length_count(string_list):
    counter = 0
    for string in string_list:
        if len(string) >=2 and string[0] == string[-1]:
            counter += 1
            return counter

string_list=['aa','bbs','ccc']
result = length_count(string_list)
print(result)