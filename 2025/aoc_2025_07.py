from pathlib import Path

cwd = Path(__file__).parent / "Inputs" / f"{Path(__file__).stem}.txt"

with open(cwd, encoding="utf-8") as f:
    lines = [line.rstrip('\n') for line in f]

def find_start(line : str) -> int:
    return line.find("S")

def func1():
    start = find_start(lines[0])
    beam_indecies = set()
    beam_indecies.add(start)
    total_splits = 0
    for line in lines[1:]:
        splitter_indecies = [i for i in range(len(line)) if line.startswith("^", i)]
        if splitter_indecies:
            for splitter in splitter_indecies:
                if splitter in beam_indecies:
                    total_splits += 1
                    beam_indecies.add(splitter-1)
                    beam_indecies.add(splitter+1)
                    beam_indecies.remove(splitter)
            splitter_indecies = []
    return(total_splits)
        


def func2():
    start = find_start(lines[0])
    beam_counts = {start: 1}
    total_paths = 0
    for line in lines[1:]:
        splitter_indecies = [i for i in range(len(line)) if line.startswith("^", i)]
        new_beam_counts = {}
        if splitter_indecies:
            for index, count in beam_counts.items():
                if index in splitter_indecies:
                    new_beam_counts[index - 1] = new_beam_counts.get(index - 1, 0) + count
                    new_beam_counts[index + 1] = new_beam_counts.get(index + 1, 0) + count
                else:
                    # passes straight through, unaffected
                    new_beam_counts[index] = new_beam_counts.get(index, 0) + count            
            beam_counts = new_beam_counts
            splitter_indecies = []
        # if no splitters this row, beam_counts stays the same (beams just fall through)

    total_paths = sum(beam_counts.values())
    return total_paths
            


if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')