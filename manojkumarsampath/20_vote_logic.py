#20. Write a program to check whether a person
# can vote (age >= 18) using logical operators

def can_vote(age):
    if age >= 18:
        return True
    else:
        return False

age = 21

if can_vote(age):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
