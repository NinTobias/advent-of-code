from itertools import combinations
from math import dist, prod
from pathlib import Path

cwd = Path(__file__).parent / "Inputs" / f"{Path(__file__).stem}.txt"

with open(cwd, encoding='utf-8') as f:
    lines = [line.rstrip('\n') for line in f]
    lines = [[int(coord) for coord in line.split(",")] for line in lines]

def generate_distances(points):
    return sorted([
        [dist(points[index1], points[index2]), index1, index2]
        for index1, index2 in combinations(range(len(points)), 2)
        ], key= lambda x: x[0])

def find_representative(parent, i):
    if i == parent[i]:
        return i
    next_parent_id = parent[i]
    return find_representative(parent, next_parent_id)

def union(parent, i, j):
    i_rep = find_representative(parent, i)
    j_rep = find_representative(parent, j)
    if i_rep != j_rep:
        parent[i_rep] = j_rep
    return parent

def get_three_largest_sizes(parent : list[int]):
    tally = {}
    for i in range(len(parent)):
        current_representative = find_representative(parent, i)
        current_count = tally.get(current_representative, 0)
        tally[current_representative] = current_count + 1
    return sorted(tally.values(), reverse=True)[:3]

def union_output(parent, i, j):
    i_rep = find_representative(parent, i)
    j_rep = find_representative(parent, j)
    if i_rep != j_rep:
        parent[i_rep] = j_rep
        return True, i, j
    return False, i, j

def func1():
    parent = list(range(len(lines)))
    distances = generate_distances(lines)
    for distance in distances[:1000]:
        union(parent, distance[1], distance[2])
    return prod(get_three_largest_sizes(parent))

def func2():
    parent = list(range(len(lines)))
    distances = generate_distances(lines)
    p1, p2 = 0, 0
    for distance in distances:
        is_current_last_pair, i, j = union_output(parent, distance[1], distance[2])
        if is_current_last_pair:
            p1, p2 = lines[i], lines[j]
    return p1[0] * p2[0]

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')