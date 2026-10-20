from pathlib import Path
from os import path
import re

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    temp = [line.rstrip('\n') for line in f]
    line = "".join(temp)

def multiply_instruction(instruction: str) -> str:
    instr = instruction.replace("mul(", "").replace(")", "").split(",")
    return int(instr[0]) * int(instr[1])

def func1():
    instructions = re.findall("mul\(\d+,\d+\)", line)
    return sum(multiply_instruction(instruction) for instruction in instructions)

def func2():
    instructions = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
    valid_instructions = []
    copy_element = True
    for instruction in instructions:
        if instruction == "do()":
            copy_element = True
        elif instruction == "don't()":
            copy_element = False
        elif copy_element:
            valid_instructions.append(instruction)
    return sum(multiply_instruction(instruction) for instruction in valid_instructions)

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')