def greet_user(name):
    return f"Hello, {name}!"

def uppercase_decorator(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper

def lowercase_decorator(func):
    def wrapper(name):
        return func(name).lower()
    return wrapper

greet_user = uppercase_decorator(greet_user)

print(greet_user("John"))




