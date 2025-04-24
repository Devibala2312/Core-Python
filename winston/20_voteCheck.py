# Write a program to check whether a person can vote (age >= 18) using logical operators

def check_voting(inputAge):
    if inputAge >= 18:
        return 'Great, You can vote!'
    else:
        return 'Sorry, You cannot vote!'

print('Status is: ', check_voting(44))