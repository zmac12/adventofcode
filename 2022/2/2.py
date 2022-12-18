with open('input.txt', 'r') as file:
    games = file.read()

rock = ['A', 'X', 1]
paper = ['B', 'Y', 2]
scissors = ['C', 'Z', 3]
win = 6
draw = 3
loss = 0

for game in games:
