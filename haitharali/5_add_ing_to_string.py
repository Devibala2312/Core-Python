def add_ing(value):
    print("actual string", value)
    if len(value) >= 3:
        value = value + "ing"
    print("updated string", value)


add_ing("haithar")
add_ing("ha")
