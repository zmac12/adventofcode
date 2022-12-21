with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

x_coords = [1, 5, 9, 13, 17, 21, 25, 29, 33]

y_coords = [x for x in range(7, -1, -1)]

stacks = [ [] for x in x_coords]

for y in y_coords:
    for idx, x in enumerate(x_coords):
        if lines[y][x] == ' ':
            continue
        else:
            stacks[idx].append(lines[y][x])

print(stacks)

instructions = []
for line in lines[10:]:
    if len(line) == 18:
        instructions.append([int(line[5]), int(line[12]), int(line[17])])
    else:
        instructions.append([int(line[5:7]), int(line[13]), int(line[18])])

for instruction_set in instructions:
    intermediate_stack = []
    # Stacks are 0 based whereas stacks in input are 1 based
    from_stack = stacks[instruction_set[1] - 1]
    to_stack = stacks[instruction_set[2] - 1]
    # Number to move out of stack could be greater than length of stack
    num_to_move = instruction_set[0]
    len_from_stack = len(from_stack)
    num_to_move = min(num_to_move, len_from_stack)
    for idx in range(0, num_to_move):
        intermediate_stack.append(from_stack.pop())
    for idx in range(0, num_to_move):
        to_stack.append(intermediate_stack.pop())

final = ''
for stack in stacks:
    final+=(stack[-1])

print(stacks)

print(final)



# List of stacks, one stack per number in input

