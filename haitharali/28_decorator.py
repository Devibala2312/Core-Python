# 28. Decorator:
# Create a function called greet_user(name) that returns a string:
# "Hello, <name>!" (where <name> is the input parameter).
#
# Write a decorator called uppercase_decorator that modifies the function
# it decorates so that the returned string is converted to uppercase.

def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper

@uppercase_decorator
def greet_user(name: str):
    return f"Hello {name}!"

print(greet_user('HaitharAli'))
