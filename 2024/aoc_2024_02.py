from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]
    formated_lines = [[int(num) for num in line.split()] for line in lines]

def helper_func(line: list[int]) -> bool:
    """
    Determines if a given list of integers is either strictly increasing or strictly decreasing
    with a difference of 1 to 3 between consecutive elements.

    Args:
        line (list[int]): A list of integers to be checked.

    Returns:
        bool: True if the list is either strictly increasing or strictly decreasing with the
              specified difference between consecutive elements, False otherwise.
    """
    # Check if the sequence is strictly increasing or strictly decreasing
    is_increasing = all(1 <= line[i+1] - line[i] <= 3 for i in range(len(line) - 1))
    is_decreasing = all(1 <= line[i] - line[i+1] <= 3 for i in range(len(line) - 1))
    return is_increasing or is_decreasing


def func1(): 
    """
    Processes a list of formatted lines and returns the count of lines that satisfy a certain condition.

    The function iterates over each line in the global variable `formated_lines` and applies the `helper_func` 
    to determine if the line meets the specified condition. It then sums up the total number of lines that 
    meet this condition.

    Returns:
        int: The count of lines that satisfy the condition defined by `helper_func`.
    """
    return sum(1 for line in formated_lines if helper_func(line))

def func2():
    """
    Checks each line in the list 'formated_lines' to see if removing any single character
    results in a string that satisfies the 'helper_func' condition.

    Returns:
        int: The count of lines that meet the condition.
    """
    return sum(1 for line in formated_lines if any(helper_func(line[:i] + line[i+1:]) for i in range(len(line))))

if __name__ == '__main__':
    #print(formated_lines)
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')

