stringsToTest = ['python', 'java', 'h', 'hi', 'javascript']

for string in stringsToTest:
    if len(string) < 2:
        print("")
    else:
        print(string[0:2] + string[-2:])

