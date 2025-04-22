# 24. Write a function print_user_info(**kwargs) that accepts any number of keyword arguments and
# prints them in key: value format.

def print_user_info(**kwargs):
    for kwarg in kwargs:
        print(f"{kwarg}:{kwargs[kwarg]}")


print_user_info(name="haithar", id="i22250")
