from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)] # N, E, S, W

def find_starting_point():
    for y, stuff in enumerate(lines):
        for x, char in enumerate(stuff):
            if char == '^':
                return y, x

def func1():
    """
    Simulates a path traversal on a grid and returns the number of unique fields visited.

    The function starts from a given starting point and moves in a specified direction
    until it encounters a boundary or an obstacle ('#'). When an obstacle is encountered,
    the direction changes in a clockwise manner. The function keeps track of all unique
    fields visited during the traversal.

    Returns:
        int: The number of unique fields visited plus one.
    """

    # Initialize the list of visited fields with the starting point
    visited_fields = [find_starting_point()]
    # Set the initial coordinates and direction
    y, x, direction = visited_fields[0][0], visited_fields[0][1], 0
    
    # Traverse the grid until a boundary or obstacle is encountered
    while 0 <= x + DIRECTIONS[direction][0] < len(lines) and 0 <= y + DIRECTIONS[direction][1] < len(lines[0]):
        # Check if the next position is an obstacle
        if lines[y + DIRECTIONS[direction][1]][x + DIRECTIONS[direction][0]] == '#':
            # Change direction clockwise
            direction = (direction + 1) % 4
        else:
            # If the current position is not already visited, add it to the list
            if (y, x) not in visited_fields:
                visited_fields.append((y, x))
            # Move to the next position
            y, x = y + DIRECTIONS[direction][1], x + DIRECTIONS[direction][0]
    
    # Return the number of unique fields visited plus one (the ending point)
    return len(visited_fields) + 1

def func2():
    """
    Simulates a path traversal on a grid and returns the total number of ways to get stuck in
    an infinite loop by adding an additional obstacle. 

    The function starts from a given starting point and moves in a specified direction
    until it encounters a boundary or an obstacle ('#'). When an obstacle is encountered,
    the direction changes in a clockwise manner. The function keeps track of all unique
    fields visited during the traversal. It tries every possible new obstacle location.

    Returns:
        int: The total number of ways to get stuck in an infinite loop.
    """

    # Initialize the list of visited fields with the starting point
    visited_fields = [find_starting_point()]
    # Set the initial coordinates and direction
    y, x, direction, loops = visited_fields[0][0], visited_fields[0][1], 0, 0

    # Check every possible obstacle location
    for y_obstacle in range(len(lines)):
        for x_obstacle in range(len(lines[0])):
            # Skip the starting point
            if y_obstacle == y and x_obstacle == x:
                continue
            # Skip the obstacle if it is already an obstacle
            if lines[y_obstacle][x_obstacle] == '#':
                continue
            # Traverse the grid until a boundary or obstacle is encountered
            visited_positions = set()
            consecutive_visits = 0
            while 0 <= x + DIRECTIONS[direction][0] < len(lines) and 0 <= y + DIRECTIONS[direction][1] < len(lines[0]):
                # Check if the next position is an obstacle
                if lines[y + DIRECTIONS[direction][1]][x + DIRECTIONS[direction][0]] == '#':
                    # Change direction clockwise
                    direction = (direction + 1) % 4
                else:
                    # If the current position is not already visited, add it to the list
                    if (y, x) not in visited_fields:
                        visited_fields.append((y, x))
                    # Move to the next position
                    y, x = y + DIRECTIONS[direction][1], x + DIRECTIONS[direction][0]
                    # Check if the current position has been visited before
                    if (y, x) in visited_positions:
                        consecutive_visits += 1
                        if consecutive_visits > 1:
                            loops += 1
                            break
                    else:
                        consecutive_visits = 0
                    visited_positions.add((y, x))
                


    return loops

if __name__ == '__main__':
    #print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')