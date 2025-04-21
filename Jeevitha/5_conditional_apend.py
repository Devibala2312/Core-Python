def conditional_append(input):
    return input if len(input) < 3 else (input +'ly' if input.endswith('ing') else input+'ing')
    
input = 'Adding'
print(conditional_append(input))

input = 'Add'
print(conditional_append(input))

input = 'Ad'
print(conditional_append(input))
