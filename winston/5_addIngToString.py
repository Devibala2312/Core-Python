def appending_to_string(inputString):
    if len(inputString) >= 3:
        if inputString.endswith('ing'):
            inputString+= 'ly'
        else:
            inputString+= 'ing'
        # print(inputAge)
        return inputString
    else:
        return inputString

print(appending_to_string('cursor'))