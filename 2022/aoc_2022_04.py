from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]

def func1():
    pairs = 0
    for line in lines:
        elf1, elf2 = line.split(",")
        elf1_section1, elf1_section2 = elf1.split("-")
        elf2_section1, elf2_section2 = elf2.split("-")
        if int(elf1_section1) <= int(elf2_section1) and int(elf1_section2) >= int(elf2_section2):
            pairs += 1
        elif int(elf1_section1) >= int(elf2_section1) and int(elf1_section2) <= int(elf2_section2):
            pairs += 1
    return pairs

def func2():
    pairs = 0
    for line in lines:
        elf1, elf2 = line.split(",")
        elf1_section1, elf1_section2 = elf1.split("-")
        elf2_section1, elf2_section2 = elf2.split("-")
        if int(elf2_section1) <= int(elf1_section1) <= int(elf2_section2):
            pairs += 1
        elif int(elf2_section1) <= int(elf1_section2) <= int(elf2_section2):
            pairs += 1
        elif int(elf1_section1) <= int(elf2_section1) and int(elf1_section2) >= int(elf2_section2):
            pairs += 1
    return pairs

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')