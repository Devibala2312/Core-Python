def getConcatString(input):
    if len(input) < 2:
        return input
    return input[:2] + input[-2:]

getConcatString("Hello World")