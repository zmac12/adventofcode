with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

badges = []

for i in range(0, len(lines) - 2, 3):
    badge = 0
    c1, c2, c3 = [*lines[i]], [*lines[i+1]], [*lines[i+2]]
    for item in c1:
        if item in c2 and item in c3:
            if item.islower():
                badge += ord(item) - ord('a') + 1
            if item.isupper():
                badge += ord(item) - 65 + 27
            break
    badges.append(badge)
print(sum(badges))
