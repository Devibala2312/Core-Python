def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    # print("KW args example", kwargs)

user_info(name="Prasanth", city="Chennai", country="India")