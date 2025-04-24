# 5. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string is already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged

string_input = input("Enter a string: ")

# if len(string_input) < 2:
#     print("The string is too short.")
# elif "ing"in string_input :
#     print(string_input.replace("ing", "ly"))
# else:print(string_input + "ing")

if len(string_input) < 3:
    print(string_input)
elif string_input.endswith("ing"):
    print(string_input + "ly")
else: print(string_input + "ing")