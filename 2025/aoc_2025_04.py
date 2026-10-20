from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]

def pad_input_grid(grid : list[str]) -> list[str]:
    # Pad the grid with '.' characters on all sides to avoid index errors when checking neighbors
    padded_grid = ['.' * (len(grid[0]) + 2)]  # Top padding
    for row in grid:
        padded_grid.append('.' + row + '.')  # Left and right padding
    padded_grid.append('.' * (len(grid[0]) + 2))  # Bottom padding
    return padded_grid


def func1():
    g = pad_input_grid(lines)
    count = 0
    neighbours = 0
    for y in range(1, len(g) - 1):
        for x in range(1, len(g[0]) - 1):
            neighbours = 0 
            if g[y][x] == "@":
                # collect the 8 neighbouring cells
                all_neighbors = "".join(
                    (
                        g[y + dy][x + dx]
                        for dy in (-1, 0, 1)
                        for dx in (-1, 0, 1)
                        if not (dy == 0 and dx == 0)
                    )
                )
                neighbours = all_neighbors.count("@");
                if neighbours < 4:
                    count += 1  
    return count

def func2():
    g = pad_input_grid(lines)
    count, old_count = 0, -1

    while count != old_count:
        old_count = count
        for y in range(1, len(g) - 1):
            for x in range(1, len(g[0]) - 1):
                valid_neighbours = 0 
                if g[y][x] != ".":
                    # build neighbors string more readably
                    all_neighbors = "".join(
                        (
                            g[y + dy][x + dx]
                            for dy in (-1, 0, 1)
                            for dx in (-1, 0, 1)
                            if not (dy == 0 and dx == 0)
                        )
                    )
                    valid_neighbours = sum(all_neighbors.count(valid) for valid in ("@", "X"))
                    if valid_neighbours < 4:
                        count += 1
                        g[y] = g[y][:x] + "X" + g[y][x+1:]

        for i, y in enumerate(g):
            g[i] = y.replace("X", ".")
                             
    return count

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')
