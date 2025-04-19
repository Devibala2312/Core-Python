# 1.Write a Python program to count the number of characters in a string.

str = "google.com"

print(f"test string {str}")
lower_str = str.lower()
my_dict = {}
count = len(lower_str)
for i in range(count):
    if lower_str[i] in my_dict:
        my_dict[lower_str[i]] = my_dict[lower_str[i]] + 1
    else:
        my_dict[lower_str[i]] = 1

print("dict is ", my_dict)

sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("sorted dict is", sorted_dict_desc)