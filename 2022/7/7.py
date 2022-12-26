with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

fileStructure = {'/': {}}

for command in lines:
    command = list(command)
    if command[0] == '$':
        if command[2] == 'c':
            dirname = command[5]
        elif command[2] == 'l':
            