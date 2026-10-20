from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]
    #pad the lines with "." to avoid index errors
    for i in range(len(lines)):
        lines[i] = "." + lines[i] + "."
    #pad the top and bottom of the lines with "." to avoid index errors
    lines.insert(0, "." * len(lines[0]))

def func1():
    def check_adjacent_symbols(y, x):
        for a in range(-1, 2):
            for b in range(-1, 2):
                try:
                    if lines[y + a][x + b] not in ".0123456789":
                        return True
                except IndexError:
                    pass
        return False
    sum = 0    
    current_number = ""
    has_adjacent_symbol = False
    for indy, y in enumerate(lines):
        for indx, _ in enumerate(y):
            if lines[indy][indx] in "0123456789":
                current_number += lines[indy][indx]
                if not has_adjacent_symbol:
                    has_adjacent_symbol = check_adjacent_symbols(indy, indx)
                else:
                    continue
            else:
                if has_adjacent_symbol:
                    sum += int(current_number)
                    has_adjacent_symbol = False
                    current_number = "" 
                else:
                    current_number = ""  
                    continue
    return sum

def func2():
    #TODO: finish this
    sum = 0
    current_number_1 = ""
    current_number_2 = ""
    for indy, y in enumerate(lines):
        for indx, _ in enumerate(y): 
            if lines[indy][indx] == "*":
                pass



if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')