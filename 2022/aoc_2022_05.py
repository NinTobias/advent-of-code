### Problem: cannot display both solution (because stack gets mutated)

from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'


def move_crate_and_insert_in_front(instruction):
    # weed out the pure numbers of the instructions
    parts = [int(part) for part in instruction.split(" ")[1::2]]
    # for every instruction, remove the crate and insert it on top the new stack
    for _ in range(parts[0]):
        element = crane_stacks[parts[1]-1].pop(0)
        crane_stacks[parts[2]-1].insert(0, element)
    return crane_stacks

def move_crate_and_insert_in_back(instruction):
    # weed out the pure numbers of the instructions
    parts = [int(part) for part in instruction.split(" ")[1::2]]
    # for every instruction, remove the crate and insert it on top the new stack
    temp_stack = []
    for _ in range(parts[0]):
        element = crane_stacks[parts[1]-1].pop(0)
        temp_stack.append(element)
    crane_stacks[parts[2]-1] = temp_stack + crane_stacks[parts[2]-1]
    return crane_stacks


with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]
    crane_stacks = []
        # splitting input into two parts
    crane_part, instructions = lines[:lines.index("") - 1], lines[lines.index("") + 1:]
    # taking out unimportant chars
    for index, level in enumerate(crane_part):
        crane_part[index] = ''.join(level[4*num + 1] for num in range(9))
        print(crane_part)
    # building stacks
    for x in range(len(crane_part) + 1):   # add + 1 here if it breaks
        column = "".join(level[x] for level in crane_part)
        crane_stacks.append([char for char in column if char != " "])


def func1():
    # executing instructions
    for instruction in instructions:
        move_crate_and_insert_in_front(instruction)
    return "".join([stack[0] for stack in crane_stacks])

def func2():
    # executing instructions
    for instruction in instructions:
        move_crate_and_insert_in_back(instruction)
    return "".join([stack[0] for stack in crane_stacks])

if __name__ == '__main__':
    # Problem right here!
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')