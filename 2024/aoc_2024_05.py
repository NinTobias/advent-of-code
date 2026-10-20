from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]

    raw_rules = lines[:lines.index('')]
    rules = [[int(page) for page in rule.split('|')] for rule in raw_rules]

    raw_instructions = lines[lines.index('')+1:]
    instructions = [[int(page) for page in instruction.split(',')] for instruction in raw_instructions]

def is_instruction_valid(instruction):
    for i in range(len(instruction)):
        for j in range(i+1, len(instruction)):
            if [instruction[j], instruction[i]] in rules:
                return False
    return True

def fix_instruction(instruction):
    while not is_instruction_valid(instruction):
        for i in range(len(instruction)):
            for j in range(i+1, len(instruction)):
                if [instruction[j], instruction[i]] in rules:
                    instruction[j], instruction[i] = instruction[i], instruction[j]
    return instruction

def func1():
    return sum(instruction[(len(instruction)-1)//2] for instruction in instructions if is_instruction_valid(instruction))
            

def func2():
    return sum(fix_instruction(instruction)[(len(instruction)-1)//2] for instruction in instructions if not is_instruction_valid(instruction))
                

if __name__ == '__main__':
    #print(instructions), print(rules)
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')