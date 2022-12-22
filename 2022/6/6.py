with open('input.txt', 'r') as file:
    buffer = list(file.read())

startingIdx = 0
currentValues = set()
idx = 0
while idx < len(buffer) - 4:
    if buffer[idx] in currentValues:
        startingIdx = idx
        currentValues
    idx += 1
