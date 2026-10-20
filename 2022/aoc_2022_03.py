from pathlib import Path
from os import path
import string

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]

def func1():
    priority = 0
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    for line in lines:
        front, back = set(line[:len(line)//2]), set(line[len(line)//2:])
        char = front.intersection(back).pop()
        priority += alphabet.find(char) + 1
    return priority
        

def func2():
    priority = 0
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    for k in range(len(lines)//3):
        temp = set(lines[3*k]).intersection(set(lines[3*k+1]))
        char = temp.intersection(lines[3*k+2]).pop()
        priority += alphabet.find(char) + 1
    return priority

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')