import collections
from typing import TypeAlias

# Declare TypeAliases for purposes of IDE type checking
Position: TypeAlias = tuple[int, int]
AdjacencyList: TypeAlias = dict[Position, list[Position]]

def get_char_no(char: str) -> int:
    no = ord(char) - ord('a') + 1
    return no

#Build Adj Lists
def build_adj_list(grid: list[str]) -> tuple[AdjacencyList, Position, Position]:
    adjList: AdjacencyList = collections.defaultdict(list)
    rows, cols = len(grid), len(grid[0])
    # Start grid iteration to check for start and end positions
    # Building adj list for every point along the way
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            point = (row, col)
            if char == "S":
                start: Position = point
                char = "a"
            elif char == "E":
                end: Position = point
                char = "z"
            
            neighbors = (
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            )

            current_position = get_char_no(char)
            for nrow, ncol in neighbors:
                # if neighbors are out of bounds of grid, ignore current position and continue iteration
                if nrow < 0 or nrow >= rows or ncol < 0 or ncol >= cols:
                    continue

                nchar = grid[nrow][ncol]
                # Replace start and ending positions with the lowest
                # and highest letters respectively
                if nchar == "S":
                    nchar = "a"
                elif nchar == "E":
                    nchar = "z"

                # if neighbor char is _at most_ 1 position higher, i.e. diff <= 1,
                # append neighbor to adj list due to it being a valid edge
                if get_char_no(nchar) - current_position <= 1:
                    adjList[point].append((nrow, ncol))

    return adjList, start, end

#Shortest Path
def get_shortest_path(adjList: AdjacencyList, start: Position, end: Position) -> int:
    shortest_path_seen: dict[Position, int] = {start: 0}
    # Use double-ended queue for efficient push and pop from both
    # ends of the queue
    deque = collections.deque(((start, 0), ))
    while deque:
        current_pos, steps = deque.popleft()
        next_steps = steps + 1
        for neighbor in adjList[current_pos]:
            if (
                neighbor not in shortest_path_seen
                or next_steps < shortest_path_seen[neighbor]
            ):
                shortest_path_seen[neighbor] = next_steps
                if neighbor != end:
                    deque.append((neighbor, next_steps))
    
    try:
        return shortest_path_seen[end]
    except KeyError:
        return float('inf')


def main():
    with open('input.txt', 'r') as file:
        grid = [line.strip() for line in file]

    adjList, start, end = build_adj_list(grid)

    steps = get_shortest_path(adjList, start, end)

    print(steps)
    return steps

if __name__ == '__main__':
    main()

    
