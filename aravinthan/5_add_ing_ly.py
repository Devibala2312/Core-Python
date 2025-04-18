def addIng(input):
    if len(input) < 3:
        return input
    if input[-3:] == 'ing':
        return input[:-3] + 'ly'
    return input + 'ing'

addIng("Someth")
addIng("Something")