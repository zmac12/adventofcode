with open('input.txt', 'r') as file:
    games = file.read().split('\n')

rock = ['A', 'X', 1]
paper = ['B', 'Y', 2]
scissors = ['C', 'Z', 3]
win = 6
draw = 3
loss = 0

totalScore = 0

for game in games:
    plays = game.split(' ')
    if plays == rock[0:2]:
        totalScore += 4
    elif plays == paper[0:2]:
        totalScore += 5
    elif plays == scissors[0:2]:
        totalScore += 6
    elif plays[0] == rock[0] and plays[1] == paper[1]:
        totalScore += 8
    elif plays[0] == rock[0] and plays[1] == scissors[1]:
        totalScore += 3
    elif plays[0] == paper[0] and plays[1] == scissors[1]:
        totalScore += 9
    elif plays[0] == paper[0] and plays[1] == rock[1]:
        totalScore += 1
    elif plays[0] == scissors[0] and plays[1] == paper[1]:
        totalScore += 2
    elif plays[0] == scissors[0] and plays[1] == rock[1]:
        totalScore += 7

print(totalScore)
    