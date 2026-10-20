from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]
    lines = [line.split("\t") for line in lines]

def func1():
    """Find the difference between the largest and smallest number in each line and sum them up"""
    sum = 0
    for line in lines:
        #convert each number in the line to an integer
        line = [int(x) for x in line]
        #add the difference between the largest and smallest number in the line to the sum
        sum += max(line) - min(line)
    return sum

def func2():
    """Find the difference between the only two numbers in each line that evenly divide each other and sum them up"""
    sum = 0
    for line in lines:
        #convert each number in the line to an integer
        line = [int(x) for x in line]
        #sort the line in descending order
        line.sort(reverse=True)
        #iterate over the line
        for index, number in enumerate(line):
            #iterate over the line again, starting at the next number
            for number2 in line[index+1:]:
                #if the first number is evenly divisible by the second number, add the result to the sum
                if number % number2 == 0:
                    sum += number // number2
    return sum

if __name__ == '__main__':
    print(lines)
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')