def checkVoteEligibility(age):
    if age >= 18:
        return 'Eligible to Vote'
    else:
        return 'Not Eligible to Vote'

checkVoteEligibility(15)