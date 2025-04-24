# Write a function name 'welcome' that prints a welcome message for the user using default argument,
# if user name provided that shoult print user name, otherwise default name should be printed

def welcome(name = 'Default Name'):
    print(f'The name is {name}')

welcome('God')

welcome('')

welcome()