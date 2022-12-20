with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

overlappingPairs = 0

for window in lines:
    window = window.split(',')
    c1, c2 = window[0], window[1]
    c1, c2 = [int(num) for num in c1.split('-')], [int(num) for num in c2.split('-')]
    if c1[1] >= c2[0] and c1[0] <= c2[1]:
        print(c1, c2)
        overlappingPairs += 1
    elif c2[1] >= c1[0] and c2[0] <= c1[1]:
        print(c1, c2)
        overlappingPairs += 1
    else:
        overlappingPairs += 0

print(overlappingPairs)