def createNewString(input):
    if (len(input) >= 2):
        print(f'Output for string {input}: ', input[:2] + input[-2:])
    else:
        print(f'Output for string {input}: ', )

createNewString('Godzilla')

createNewString('Go')

createNewString('G')