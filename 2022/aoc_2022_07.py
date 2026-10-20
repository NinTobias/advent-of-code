from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]
    parameters = [list(line.split(" ")) for line in lines]
    print(parameters)

def func1():
    pass

def func2():
    pass

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')