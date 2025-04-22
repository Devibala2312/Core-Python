# 20. Write a program to check whether a person can vote (age >= 18) using logical operators

def eligible_voter(age):
    eligible = 'eligible' if age >=18 else 'not eligible'
    print(f'The person with age {age} is {eligible} to vote')

eligible_voter(19)
eligible_voter(14)