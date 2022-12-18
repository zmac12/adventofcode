with open('input.txt', 'r') as file:
    elves = file.read().strip().split('\n\n')

highestThree = [0,0,0]

def bubbleUp(x:int, y:list):
    if x > y[0]:
        y[0] = x
    for i in range(0, len(y) - 1):
        if y[i] > y[i + 1]:
            y[i + 1], y[i] = y[i], y[i + 1]

for idx, x in enumerate(elves):
    food = x.split('\n')
    calories = 0
    for food in food:
        food = int(food)
        calories += food
    
    if calories >= highestThree[0]:
        bubbleUp(calories, highestThree)

print(sum(highestThree))
