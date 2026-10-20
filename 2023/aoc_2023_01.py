from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]

def func1():
    """Combine first and last digit of each line and sum them up"""
    sum = 0
    for line in lines:
        #filter out non-digits
        digits = [char for char in line if char in "0123456789"]
        #combine first and last digit and add to sum
        sum += 10*int(digits[0]) + int(digits[-1])
    return sum


def func2():
    """Convert words to numbers, combine first and last digit of each line and sum them up"""
    CONVERSION_DICT = {"zero" : 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    sum = 0
    for line in lines:
        #convert words to numbers
        for key in CONVERSION_DICT.keys():
            line = line.replace(key, key[0] + str(CONVERSION_DICT[key]) + key[-1])
        #filter out non-digits
        digits = [char for char in line if char in "0123456789"]
        #combine first and last digit and add to sum
        sum += 10*int(digits[0]) + int(digits[-1])
    return sum


if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')