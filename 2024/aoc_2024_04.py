from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]
    transpose = [''.join(s) for s in zip(*lines)]


def func1():
    def check_horizontal():
        return sum(line.count("XMAS") + line.count("SAMX") for line in lines)

    def check_vertical():
        return sum(line.count("XMAS") + line.count("SAMX") for line in transpose)

    def check_diagonal():
        total = 0
        for i in range(len(lines)-3):
            for j in range(len(lines[0])-3):
                if lines[i][j] == "X" and lines[i+1][j+1] == "M" and lines[i+2][j+2] == "A" and lines[i+3][j+3] == "S":
                    total += 1
                if lines[i][j] == "S" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "M" and lines[i+3][j+3] == "X":
                    total += 1
                if lines[i][j+3] == "X" and lines[i+1][j+2] == "M" and lines[i+2][j+1] == "A" and lines[i+3][j] == "S":
                    total += 1
                if lines[i][j+3] == "S" and lines[i+1][j+2] == "A" and lines[i+2][j+1] == "M" and lines[i+3][j] == "X":
                    total += 1
        return total
    
    return check_horizontal() + check_vertical() + check_diagonal()

def func2():
    total = 0
    for i in range(len(lines)-2):
        for j in range(len(lines[0])-2):
            if (lines[i][j] == "M" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "S") or \
                (lines[i][j] == "S" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "M"):
                if (lines[i][j+2] == "M" and lines[i+1][j+1] == "A" and lines[i+2][j] == "S") or \
                    (lines[i][j+2] == "S" and lines[i+1][j+1] == "A" and lines[i+2][j] == "M"):
                    total += 1
    return total

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')