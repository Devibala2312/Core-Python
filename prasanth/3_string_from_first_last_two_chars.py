print("Program to get a string made of the first 2 and the last 2 chars from a given a string: ")
string = input("Enter a string value: ")
if len(string) >= 2:
    newString = string[:2] + string[-2:]
    print("Newly created string is", newString)
else:
    print("String length less than 2")