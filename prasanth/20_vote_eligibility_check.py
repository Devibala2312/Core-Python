def eligibility_check(age):
    return 'eligible' if age >= 18 else 'not eligible'

age_value = int(input("Enter the person age: "))
print(f"The user is {eligibility_check(age_value)} to vote")