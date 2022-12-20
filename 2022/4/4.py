with open('input.txt', 'r') as file:
    lines = file.read().split('\n')

for window in lines:
    window = window.split(',')
    c1, c2 = window[0], window[1]
    c1, c2 = [int(num) for num in c1.split('-')], [int(num) for num in c2.split('-')]
    