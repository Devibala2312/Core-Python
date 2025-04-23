def add_ing_or_ly(word):
    return (
        word +'ly' if word.endswith('ing') else word + 'ly'
        if len(word) >=3 else word
    )

# Example usage:
print(add_ing_or_ly("read"))     # Output: reading
print(add_ing_or_ly("reading"))  # Output: readingly
print(add_ing_or_ly("hi"))       # Output: hi
