from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    line = f.readline().rstrip('\n')


def expand_file_deprecated():
    free_spaces = []
    files_with_id = []
    for i in range(0, len(line), 2):
        try:
            files_with_id.append(str(i//2)*int(line[i]))
            free_spaces.append(int(line[(i+1)])*".")
        except IndexError:
            if len(files_with_id) != len(free_spaces):
                free_spaces.append("")
    return "".join([f"{x}{y}" for x, y in zip(files_with_id, free_spaces)])

def expand_file():
    free_spaces = []
    files_with_id = []
    for i in range(len(line)):
        if i % 2 == 0:
            files_with_id.append(str(i//2)*int(line[i]))
        else:
            free_spaces.append(int(line[i])*".")

    return [val for pair in zip(files_with_id, free_spaces) for val in pair]

def compress_file(expanded_file: str) -> str:
    """Compact the files by moving the rightmost block to the leftmost free space."""
    blocks = list(expanded_file)  # Convert string to a mutable list
    while '.' in blocks:
        first_free_spot = blocks.index('.')
        rightmost_block = blocks[-1]

        if rightmost_block == '.':
            blocks.pop()
        else:
            blocks[first_free_spot] = rightmost_block
            blocks.pop()
    return ''.join(blocks)

def func1():
    file = compress_file(expand_file())
    return sum(i * int(file[i]) for i in range(len(file)))

def func2():
    pass

if __name__ == '__main__':
    print(expand_file())
    #print(compress_file(expand_file()))
    #print(f'Solution Part A: {func1()}')
    #print(f'Solution Part B: {func2()}')