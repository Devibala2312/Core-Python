# 1.Write a Python program to count the number of characters in a string.

str = "google.com"

def count_characters(str):
    char_count = {}
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

result = count_characters(str)
print(result)

sorted_dict_desc = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

print("sorted dict is", sorted_dict_desc)