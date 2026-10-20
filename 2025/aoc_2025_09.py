from itertools import combinations
from pathlib import Path

from shapely.geometry.polygon import Polygon

cwd = Path(__file__).parent / "Inputs" / f"{Path(__file__).stem}.txt"

with open(cwd, encoding='utf-8') as f:
    lines_initial = [line.rstrip('\n') for line in f]
    lines = [[int(coord) for coord in line.split(",")] for line in lines_initial]
    coords = [tuple(int(coord) for coord in line.split(",")) for line in lines_initial]

def calculate_area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def func1():
    return max(calculate_area(line1, line2) for line1, line2 in combinations(lines, 2))

def func2():
    polygon = Polygon(coords)
    return max(
        calculate_area(coord1, coord2) 
        for coord1, coord2 in combinations(coords, 2) 
        if polygon.contains(
            Polygon([(coord1[0], coord1[1]), (coord1[0], coord2[1]),
                     (coord2[0], coord2[1]), (coord2[0], coord1[1])])
        ))

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')