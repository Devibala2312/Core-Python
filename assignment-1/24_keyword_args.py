# keyword arguments

def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Yosuva", age=25, location="India")
