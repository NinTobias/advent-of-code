from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f][0]   # str
    print(lines)

def func1(packet_length):
    block = ""
    for index, char in enumerate(lines):
        if len(block) < packet_length:
            block += char
        elif len(set(block)) == packet_length:
            return index
        else:
            block = block[1:] + char
    return("Gibts net :(")

def func2():
    pass

if __name__ == '__main__':
    print(f'Solution Part A: {func1(4)}')
    print(f'Solution Part B: {func1(14)}')