from typing import TypeAlias

Coordinate: TypeAlias = tuple[int, int]

max_x, max_y, min_x, min_y = 0

def convert_to_coord_add_to_set(coord_list:list[str], container:set):
    for idx,coord in enumerate(coord_list):
        x,y = int(coord.split(',')[0]), int(coord.split(',')[1])
        if x > max_x:
            max_x = x
        elif x < min_x and x>= 0:
            min_x = x
        if y > max_y:
            max_y = y
        elif y < min_y and y>= 0:
            min_y = y
        coord_list[idx] = (x, y)
    for idx in range(0, len(coord_list) - 2):
        x, y = coord_list[idx][0], coord_list[idx][1]
        x_1, y_1 = coord_list[idx + 1][0], coord_list[idx + 1][1]
        if x != x_1:
            start = min(x, x_1)
            end = max(x, x_1)
            constant = y
            mode = 'horizontal'
        else:
            start = min(y, y_1)
            end = max(y, y_1)
            constant = x
            mode = 'vertical'
        for num in range(start, end + 1):
            if mode == 'horizontal':
                container.add((num, constant))
            elif mode == 'vertical':
                container.add((constant, num))

def simulate_sand(container:set):
    start_x, start_y = 500, 0

    abyss = False
    while abyss == False:
        #drop sand
        sand_location = (start_x, start_y)
        filled_this_iteration = False
        while sand_location[0] <= max_x and sand_location[1] <= max_y and sand_location[0] >= min_x and sand_location[1] >= min_y and filled_this_iteration == False:
            if (sand_location[0], sand_location[1] + 1) not in container:
                sand_location = (sand_location[0], sand_location[1] + 1)
                continue
            if (sand_location[0] - 1, sand_location[1] + 1) not in container:
                sand_location = (sand_location[0] - 1, sand_location[1] + 1)
                continue
            if (sand_location[0] + 1, sand_location[1] + 1) not in container:
                sand_location = (sand_location[0] + 1, sand_location[1] + 1)
                continue
            container.add(sand_location)
            filled_this_iteration == True
        abyss == True


def main():
    with open('input.txt', 'r') as file:
        corners_pre_split = file.read().split('\n')

    corners = [line.split(' -> ') for line in corners_pre_split]
    
    filled = set()
    for list_of_corners in corners:
        convert_to_coord_add_to_set(list_of_corners, filled)
    
    simulate_sand(filled)
    

if __name__ == '__main__':
    main()