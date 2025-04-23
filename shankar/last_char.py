def last_char(input_string):
    if len(input_string) < 2:
        return ''
    return input_string[:2]+ input_string[-2:]

print(last_char("te"))