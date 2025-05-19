def uppercase_decorator(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper


@uppercase_decorator
def greet_user(name):
    return f"Hello, {name}!"


print(greet_user("Alice"))


