with open('input.txt', 'r') as file:
    elves = file.read().strip().split('\n\n')

highest = 0

for idx, x in enumerate(elves):
    food = x.split('\n')
    calories = 0
    for food in food:
        food = int(food)
        calories += food
    
    if calories >= highest:
        highest = calories

print(highest)



