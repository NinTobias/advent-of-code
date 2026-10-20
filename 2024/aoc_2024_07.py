from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]
    results = [int(line.split(": ")[0]) for line in lines]
    operands = [[int(num) for num in line.split(": ")[1].split()] for line in lines]


def generate_operator_chains(length):
    """Generates all possible operator chains of a given length. The operators are '+' and '*'."""
    if length == 1:
        return ['+', '*']
    else:
        return [f'{op} {chain}' for op in ['+', '*'] for chain in generate_operator_chains(length - 1)]
    
def generate_operator_chains_with_concatenation(length):
    """Generates all possible operator chains of a given length. The operators are '+' and '*'
    as well as string concatenation."""
    if length == 1:
        return ['+', '*', '||']
    else:
        return [f'{op} {chain}' for op in ['+', '*', '||'] for chain in generate_operator_chains_with_concatenation(length - 1)]
        
def evaluate_chain(operator_chain, operands):
    chain = operator_chain.split()
    result = operands[0]
    for i in range(len(chain)):
        if chain[i] == '+':
            result += operands[i + 1]
        elif chain[i] == '*':
            result *= operands[i + 1]
        elif chain[i] == '||':
            result = int(str(result) + str(operands[i + 1]))
    return result

def func1():
    total = 0
    for result, operand in zip(results, operands):
        possible_chains = generate_operator_chains(len(operand) - 1)
        for chain in possible_chains:
            if evaluate_chain(chain, operand) == result:
                total += result
                break
    return total


def func2():
    total = 0
    for result, operand in zip(results, operands):
        possible_chains = generate_operator_chains_with_concatenation(len(operand) - 1)
        for chain in possible_chains:
            if evaluate_chain(chain, operand) == result:
                total += result
                break
    return total
                

if __name__ == '__main__':
    #print(evaluate_chain('+ * + *', [1, 2, 3, 4, 5]))
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')