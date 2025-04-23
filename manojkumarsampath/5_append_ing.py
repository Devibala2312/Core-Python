#5. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string is already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged

def add_ing_or_ly(word):
    if len(word) < 3:
        return word
    if word.endswith('ing'):
        return word + 'ly'
    return word + 'ing'

# Example usage
print(add_ing_or_ly("Code"))
print(add_ing_or_ly("Programming"))
print(add_ing_or_ly("go"))
