from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]

def determine_2digit_maximum_joltage(s : str) -> int:
    """Determine the maximum 2 digit joltage that can be formed from a 
    string of digits. Joltage is defined as the maximum n-digit 
    number that can be formed from the digits in the string."""
    max, current = 0, 0
    p1, p2 = 0, 0
    for i in range(0, len(s)):
        for j in range(i+1, len(s)):
            p1, p2 = s[i], s[j]
            current = 10*int(p1) + int(p2)
            if current > max:
                max = current
    return max

def determine_n_digit_maximum_joltage(s: str, n: int) -> int:
    start = 0
    digits = []
    for k in range(n):
        end = len(s) - (n - k) + 1
        max_digit = -1
        max_pos = start
        for i in range(start, end):
            d = int(s[i])
            if d > max_digit:
                max_digit = d
                max_pos = i
        digits.append(str(max_digit))
        start = max_pos + 1
    return int("".join(digits))

def func1():
    return sum(determine_n_digit_maximum_joltage(line, 2) for line in lines)

def func2():
    return sum(determine_n_digit_maximum_joltage(line, 12) for line in lines)

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')