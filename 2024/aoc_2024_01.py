from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]
    formated_list = [line.split() for line in lines]
    sorted_left_list = sorted([int(line[0]) for line in formated_list])
    sorted_right_list = sorted([int(line[1]) for line in formated_list])

def func1():
    return sum([abs(sorted_left_list[i] - sorted_right_list[i]) for i in range(len(sorted_left_list))])

def func2(): 
    return sum([sorted_right_list.count(location_ID) * location_ID for location_ID in sorted_left_list])

if __name__ == '__main__':
    #print([line.split("   ") for line in lines])
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')