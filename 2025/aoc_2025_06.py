from pathlib import Path

cwd = Path(__file__).parent / "Inputs" / f"{Path(__file__).stem}.txt"

with open(cwd, encoding="utf-8") as f:
    lines = [line.rstrip('\n') for line in f]
    cleaned_lines = [line.split() for line in lines]


def func1():
    return sum(
        sum(values) if op == "+" else values[0] * values[1] * values[2] * values[3]
        for a, b, c, d, op in zip(*cleaned_lines)
        for values in [list(map(int, (a, b, c, d)))]
    )

def func2():
    cleaned_lines_horizontal = []
    for index in range(len(cleaned_lines[0])):
        cleaned_lines_horizontal.append(
            [cleaned_lines[0][index], cleaned_lines[1][index], 
             cleaned_lines[2][index], cleaned_lines[3][index]]
            )
        
    transposed_lines = []
    for line in cleaned_lines_horizontal:
        length = len(max(line, key=len))
        transpose = []
        for _ in range(length):
            compound = ""
            for index, s in enumerate(line):
                try:
                    compound += s[-1]
                    line[index] = s[:-1]
                except IndexError:
                    pass
            transpose.append(compound)
        transposed_lines.append(transpose)
    transposed_lines.append(cleaned_lines[4])

    print(transposed_lines)

    return sum(
        sum(values) if op == "+" else values[0] * values[1] * values[2] * values[3]
        for a, b, c, d, op in zip(*transposed_lines)
        for values in [list(map(int, (a, b, c, d)))]
    )
            


if __name__ == '__main__':
    #print(cleaned_lines)
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')