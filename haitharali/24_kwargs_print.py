# 24. Write a function print_user_info(**kwargs) that accepts any number of keyword arguments and
# prints them in key: value format.

def print_user_info(**kwargs):
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")


print_user_info(name="haithar", id="i22250")
