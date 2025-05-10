# 20. Write a program to check whether a person can vote (age >= 18) using logical operators

def check_voting_eligibility(age):
    if age >=18:
        print(f'{age} is eligible to vote')
    else:
        print(f'{age} is not eligible to vote')

age = int(input('Enter a age'))
check_voting_eligibility(age)