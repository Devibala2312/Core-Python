# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead the empty string
def convert_string(value):
    if len(value) >= 2:
        new_char = value[:2] + value[-2::]
    else:
        new_char = ""
    print(new_char)


convert_string("test_string")
convert_string("ab")
convert_string("a")
