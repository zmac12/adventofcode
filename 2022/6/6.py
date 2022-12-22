with open('input.txt', 'r') as file:
    buffer = list(file.read())

startingIdx = 0
idx = 0
while idx < len(buffer) - 4:
    s = buffer[idx:(idx + 4)]
    if len(set(s)) == 4:
        print(idx + 4)
        break
    idx += 1

