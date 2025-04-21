#add "ly" or "ing" to the end of a string

def add_ly_or_ing(x):   
    if len(x) < 3:
        return x
    elif x[-3:] == "ing":
        x += "ly"
    else:
        x += "ing"
    return x

print(add_ly_or_ing("str"))

