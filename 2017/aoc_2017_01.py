from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    #only one line in this file
    line = [line.rstrip('\n') for line in f][0]

def func1():
    """Compare each digit with the previous one and sum them up if they are equal"""
    sum = 0
    #enumerate to get the index of the current digit
    for index, _ in enumerate(line):
        #if the current digit is equal to the previous one, add it to the sum
        if line[index] == line[index-1]:
            sum += int(line[index])
    return sum

def func2():
    """Compare each digit with the digit halfway around the circular list and sum them up if they are equal"""
    sum = 0
    #enumerate to get the index of the current digit
    for index, _ in enumerate(line):
        #if the current digit is equal to the digit halfway around the circular list, add it to the sum
        if line[index] == line[index-len(line)//2]:
            sum += int(line[index])
    return sum

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')