import json
import ast

def compare(a, b):
    if isinstance(a, list) and isinstance(b, int):
        b = [b]
    if isinstance(b, list) and isinstance(a, int):
        a = [a]
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        elif a == b:
            return 0
        else:
            return -1
    
    if isinstance(b, list) and isinstance(a, list):
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            x = compare(a[i], b[j])
            if x == 1:
                return 1
            if x == -1:
                return -1

            i += 1
            j += 1

        if i == len(a):
            if j == len(b):
                return 0
            return 1

        if j == len(b):
            return -1 
        
        return 0

            

def main():
    with open('./input.txt', 'r') as file:
        packets = file.read().strip().split('\n\n')
    ans = 0
    for idx, block in enumerate(packets):
        a, b = map(eval, block.split('\n'))
        res = compare(a, b)
        if res == 1:
            print(idx + 1)
            ans += idx + 1
    print(ans)
if __name__ == '__main__':
    main()