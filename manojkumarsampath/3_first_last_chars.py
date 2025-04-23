#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead the empty string

def first_last_2_chars(input_string):
    if len(input_string) < 2:
        return ''
    return input_string[:2] + input_string[-2:]

print(first_last_2_chars('Python Programming'))
print(first_last_2_chars('w'))
print(first_last_2_chars('Python'))