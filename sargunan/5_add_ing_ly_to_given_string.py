# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string is already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged

def add_ing_ly(string):
    if len(string) < 3:
        return string
    elif string.endswith('ing'):
        return string + 'ly'
    else:
        return string + 'ing'

print(add_ing_ly('ea'))
print(add_ing_ly('fast'))
print(add_ing_ly('thinking'))