# "24. Write a function print_user_info(**kwargs) that accepts any number of keyword arguments and
# prints them in key: value format."

def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
print_user_info(name="Alice", age=25, city="NYC")