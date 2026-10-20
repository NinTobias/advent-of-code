from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]

def func1():
    totals = []
    cur_max = 0
    for line in lines:
        if line == "": 
            totals.append(cur_max)
            cur_max = 0
        else:
            cur_max += int(line)
    totals.sort(reverse=True)
    return totals

if __name__ == "__main__":
    print(f"Solution Part A: {func1()[0]}")
    print(f"Solution Part B: {sum(func1()[:3])}")






