with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

for rucksack in lines:
    rucksack = [*rucksack]
    c1, c2 = rucksack[0:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):len(rucksack)]
    