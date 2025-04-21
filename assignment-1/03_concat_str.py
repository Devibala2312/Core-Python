#concatenate first two and last two characters of a string

def concat_first_last(str1):
    if len(str1) < 2:
        return ""
    else:
        return f"{str1[:2]}{str1[-2:]}"
    
print(concat_first_last("hello"))



