string = input("Enter the string value: ")

# def add_ing_or_ly(word):
#     if len(word)>2:
#         if word.endswith("ing"):
#             print(word[:-3] + "ly")
#         else:
#             print(word + "ing")
#     else:
#         print(word)

def add_ing_or_ly(word):
    if len(word)>2:
        return word[:-3]+"ly" if word.endswith("ing") else word + "ing"
    return word

print("Updated word:", add_ing_or_ly(string))