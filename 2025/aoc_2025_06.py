from math import prod
from pathlib import Path

cwd = Path(__file__).parent / "Inputs" / f"{Path(__file__).stem}.txt"

with open(cwd, encoding="utf-8") as f:
    lines = [line.rstrip('\n') for line in f if line.strip()]
    cleaned_lines = [line.split() for line in lines]


def func1():
    *number_rows, operators = cleaned_lines
    total = 0
    for *values, op in zip(*number_rows, operators):
        numbers = list(map(int, values))
        print(numbers)
        total += sum(numbers) if op == "+" else prod(numbers)
    return total

def func2():
    *number_rows, operators = lines
    columns = list(zip(*number_rows))[::-1]

    groups, current_group = [], []
    for column in columns:
        if all(char == " " for char in column):
            if current_group:
                groups.append(current_group)
                current_group = []
        else:
            current_group.append(int("".join(column).strip()))

    if current_group:
        groups.append(current_group)

    total, ops = 0, operators.split()[::-1]
    for group, op in zip(groups, ops):
        total += sum(group) if op == "+" else prod(group)
    return total

if __name__ == '__main__':
    print(cleaned_lines)
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')