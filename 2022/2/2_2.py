with open('input.txt', 'r') as file:
    games = file.read().split('\n')

rock = ['A', 'X', 1]
paper = ['B', 'Y', 2]
scissors = ['C', 'Z', 3]
win = 6
draw = 3
loss = 0

wins = {'A': 8, 'B': 9, 'C': 7}
losses = {'A': 3, 'B': 1, 'C': 2}
draws = {'A': 4, 'B': 5, 'C': 6}


totalScore = 0

for game in games:
    plays = game.split(' ')
    if plays[1] == 'X':
        totalScore += losses.get(plays[0])
    elif plays[1] == 'Y':
        totalScore += draws.get(plays[0])
    else:
        totalScore += wins.get(plays[0])

print(totalScore)