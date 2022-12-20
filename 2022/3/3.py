

with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

priorities = []

for rucksack in lines:
    priority = 0
    rucksack = [*rucksack]
    c1, c2 = rucksack[0:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):len(rucksack)]
    for item in c1:
        if item in c2:
            if item.islower():
                priority += ord(item) - ord('a') + 1
            if item.isupper():
                priority += ord(item) - 65 + 27
            break
    priorities.append(priority)

print(sum(priorities))