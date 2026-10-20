from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]
    print(lines)

def func1():
    total = 0
    point_matrix = [[4, 8, 3], [1, 5, 9], [7, 2, 6]]
    for line in lines:
        translated_line = line.replace("A", "0").replace("B", "1").replace("C", "2").replace("X", "0").replace("Y", "1").replace("Z", "2")
        total += point_matrix[int(translated_line[0])][int(translated_line[2])]
    return total

def func2():
    total = 0
    point_matrix = [[3, 4, 8], [1, 5, 9], [2, 6, 7]]
    for line in lines:
        translated_line = line.replace("A", "0").replace("B", "1").replace("C", "2").replace("X", "0").replace("Y", "1").replace("Z", "2")
        total += point_matrix[int(translated_line[0])][int(translated_line[2])]
    return total

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')