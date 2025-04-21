def concat_string(input):
    if len(input) <= 2:
        return ''
    return input[:2]+input[-2:]

input = "Programming"
print(concat_string(input))


input = "Hi"
print(concat_string(input))
