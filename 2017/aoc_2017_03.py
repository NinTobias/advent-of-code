from pathlib import Path
from os import path
import math

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    line = [line.rstrip('\n') for line in f]

def func1():
    """Find the Manhattan distance from the number to the center of the spiral"""
    number = int(line[0])
    # find the concentric square-ring the number is in
    a_n = math.ceil((math.sqrt(number) - 1) / 2)
    # using the fact that the bottom right corner of each square-ring is equal to (2n + 1)^2
    # where n is the nth square-ring and it being the maximum number of the nth square-ring,
    # compute the bottom right corner of the square-ring.
    b_n = (2 * a_n + 1) ** 2
    # compute the offset from the bottom right corner of the square-ring to the number.
    # this is the distance from the number to the bottom right corner of the square-ring.
    # (wlog, the distance from the number to the bottom right corner of the square-ring is the same 
    # as the distance from the number to the center of the square-ring)
    offset = b_n - number
    # now compute the distance, which is the sum of the distance from the number to the center of the 
    # square-ring laterally outward and the distance from the number to the center of the square-ring.
    return a_n + abs(a_n - (offset % (2 * a_n)))


def func2():
    #visited coordinates and their values
    grid_dict = {(0, 0): 1}
    # directions for moving right, up, left, down respectively
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    current = grid_dict[(0, 0)]
    while True:
        print(grid_dict)
        # find the next direction to move in
        direction = directions[(len(grid_dict) - 1) % 4]
        # find the next coordinate to move to
        next_coord = (list(grid_dict.keys())[-1][0] + direction[0], list(grid_dict.keys())[-1][1] + direction[1])
        # find the next value to store in the next coordinate
        next_value = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (next_coord[0] + i, next_coord[1] + j) in grid_dict:
                    next_value += grid_dict[(next_coord[0] + i, next_coord[1] + j)]
        # store the next value in the next coordinate
        grid_dict[next_coord] = next_value
        # if the next value is greater than the input, return it
        if next_value > int(line[0]):
            return next_value


if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')