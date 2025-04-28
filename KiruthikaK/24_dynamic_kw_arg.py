def print_user_info(**userinfo):
    for k , v in userinfo.items():
        print(f"{k}:{v}")

print_user_info(name="Alice", age=25, city="NYC")