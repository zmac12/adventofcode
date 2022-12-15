from typing import TypeAlias

Coordinate: TypeAlias = tuple[int, int]

def convert_to_coord_add_to_set(coord_list:list(str), container:set):
    for idx,coord in enumerate(coord_list):
        coord_list[idx] = (int(coord.split(',')[0]), int(coord.split(',')[1]))
    for idx in range(0, len(coord_list) - 2):
        if coord_list[idx][0] != coord_list[idx + 1][0]:
            start = min(coord_list[idx][0], coord_list[idx + 1][0])
            end = max(coord_list[idx][0], coord_list[idx + 1][0])
            constant = coord_list[idx][1]
            mode = 'horizontal'
        else:
            start = min(coord_list[idx][1], coord_list[idx + 1][1])
            end = max(coord_list[idx][1], coord_list[idx + 1][1])
            constant = coord_list[idx][0]
            mode = 'vertical'
        for num in range(start, end + 1):
            if mode == 'horizontal':
                container.add(num, constant)
            elif mode == 'vertical':
                container.add(constant, num)

def main():
    with open('input.txt', 'r') as file:
        corners_pre = file.read().split('\n')

    corners = [line.split(' -> ') for line in corners_pre]
    
    filled = set()
    for list_of_corners in corners:
        convert_to_coord_add_to_set(list_of_corners, filled)
    
    print(filled)
    

if __name__ == '__main__':
    main()