# 22. Write a function name 'welcome' that prints a welcome message for the user using default
# argument, if user name provided that should print user name, otherwise default name should be printed

def welcome(name ='default'):
    print(f"name is {name}")

welcome("haithar")
welcome()