from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]
    instructions = [instruction.split(" ") for instruction in lines]
    knots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    visited = set()
    visited2 = set()

def isTouching(head : list, tail: list) -> bool:
    return abs(head[0]-tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1

def move(direction, steps, head, tail):
    for _ in range(steps):
        if direction == "U":
            head[1] += 1
            if not isTouching(head, tail):
                if head[0] != tail[0]:
                    tail[0] = head[0]
                tail[1] += 1
        if direction == "D":
            head[1] -= 1
            if not isTouching(head, tail):
                if head[0] != tail[0]:
                    tail[0] = head[0]
                tail[1] -= 1
        if direction == "R":
            head[0] += 1
            if not isTouching(head, tail):
                if head[1] != tail[1]:
                    tail[1] = head[1]
                tail[0] += 1
        if direction == "L":
            head[0] -= 1
            if not isTouching(head, tail):
                if head[1] != tail[1]:
                    tail[1] = head[1]
                tail[0] -= 1
        print(f"Head: {head}, Tail: {tail}")
        visited.add(tuple(knots[-1].copy()))
        
def func1():
    for instruction in instructions:
        move(instruction[0], int(instruction[1]), knots[0], knots[-1])
    return len(visited)

def func2():
    knots[0], knots[-1] = [0, 0], [0, 0]
    for instruction in instructions:
        for knot in range(len(knots)-1):
            move(instruction[0], int(instruction[1]), knots[knot], knots[knot+1])
        visited2.add(tuple(knots[-1].copy()))
    return len(visited2)
if __name__ == '__main__':
    print(f'Solution Part A: {func1()}') #6337
    #print(f'Solution Part B: {func2()}')


"""from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]
    instructions = [instruction.split(" ") for instruction in lines]
    head, tail = [0,0], [0,0]
    visited = set()

def isTouching(head : list, tail: list) -> bool:
    return abs(head[0]-tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1

def move(direction, steps):
    for _ in range(steps):
        if direction == "U":
            head[1] += 1
            if not isTouching(head, tail):
                if head[0] != tail[0]:
                    tail[0] = head[0]
                tail[1] += 1
        if direction == "D":
            head[1] -= 1
            if not isTouching(head, tail):
                if head[0] != tail[0]:
                    tail[0] = head[0]
                tail[1] -= 1
        if direction == "R":
            head[0] += 1
            if not isTouching(head, tail):
                if head[1] != tail[1]:
                    tail[1] = head[1]
                tail[0] += 1
        if direction == "L":
            head[0] -= 1
            if not isTouching(head, tail):
                if head[1] != tail[1]:
                    tail[1] = head[1]
                tail[0] -= 1
        print(f"Head: {head}, Tail: {tail}")
        visited.add(tuple(tail.copy()))
        
def func1():
    for instruction in instructions:
        move(instruction[0], int(instruction[1]))
    return len(visited)

def func2():
    pass

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')
"""