# "24. Write a function print_user_info(**kwargs) that accepts any number of keyword arguments and
# prints them in key: value format."

def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

user_info(name="Hello", age=25, city="Chennai")