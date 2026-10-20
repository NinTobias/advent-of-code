from pathlib import Path

cwd = Path(__file__).parent / "Inputs" / f"{Path(__file__).stem}.txt"

with open(cwd, encoding="utf-8") as f:
    lines = [line.rstrip('\n') for line in f]

def func1():
    total, zero_count = 50, 0
    for instruction in lines:
        direction, value = instruction[0], int(instruction[1:])
        if direction == 'L':
            total = (total - value) % 100
        elif direction == 'R':
            total = (total + value) % 100
        if total == 0:
            zero_count += 1
    return zero_count

def func2():
    total, zero_count = 50, 0
    for instruction in lines:
        direction, value = instruction[0], int(instruction[1:])
        if direction == 'L':
            for _ in range(value):
                total = (total - 1) % 100
                if total == 0:
                    zero_count += 1
        elif direction == 'R':
            for _ in range(value):
                total = (total + 1) % 100
                if total == 0:
                    zero_count += 1
    return zero_count

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')