# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead the empty string

def create_new_string(s):
    if len(s) > 2:
        new_str = s[:2] + s[-2:]
        return new_str
    else:
        print("Length of the string is less than 2. Cannot create a string.")
        return ''

string = input("Enter a string: ")
print("Result: ", create_new_string(string))