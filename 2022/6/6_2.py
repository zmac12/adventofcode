with open('input.txt', 'r') as file:
    buffer = list(file.read())

startingIdx = 0
idx = 0
while idx < len(buffer) - 14:
    s = buffer[idx:(idx + 14)]
    if len(set(s)) == 14:
        print(idx + 14)
        break
    idx += 1

