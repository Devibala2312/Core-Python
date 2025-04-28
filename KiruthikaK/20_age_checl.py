def can_vote(age):
    if age >= 18:
        return "eligible to vote."
    else:
        return "not eligible."

# Example usage
age = int(input("Enter your age: "))
print(can_vote(age))
