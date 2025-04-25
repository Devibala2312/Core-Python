# 20. Write a program to check whether a person can vote (age >= 18) using logical operators

def check_vote(age):
    if age >= 18:
        print("can vote")
    else:
        print("cannot vote")
        
check_vote(18)
check_vote(17)

