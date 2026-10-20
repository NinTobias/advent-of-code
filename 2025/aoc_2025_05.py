from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]
    ranges, ids = lines[:lines.index("")], lines[lines.index("")+1:]

def func1():
    parsed_ranges = []
    for r in ranges:
        start, stop = map(int, r.split("-"))
        parsed_ranges.append((start, stop))
    count = 0
    for id_str in ids:
        value = int(id_str)
        if any(start <= value <= stop for start, stop in parsed_ranges):
            count += 1
    return count

def func2():
    total_ranges = []
    for r in ranges:
        start, stop = map(int, r.split("-"))
        total_ranges.append((start, stop))

    sorted_ranges = sorted(total_ranges, key=lambda x: x[0])

    total_elements = 0
    current_start, current_end = sorted_ranges[0]

    for start, end in sorted_ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            total_elements += (current_end - current_start + 1)
            current_start, current_end = start, end
    total_elements += (current_end - current_start + 1)
    return total_elements






if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')