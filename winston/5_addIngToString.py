def appendingToString(input):
    if len(input) >= 3:
        if (input.endswith('ing')):
            input+= 'ly'
        else:
            input+= 'ing'
        # print(input)
        return input
    else:
        return input

print(appendingToString('cursor'))