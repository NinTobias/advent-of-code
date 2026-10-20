from pathlib import Path
from os import path

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd) as f:
    lines = [line.rstrip('\n') for line in f]
    tree_matrix = [[int(tree) for tree in line] for line in lines]

def truncate_list_2(l, value) -> list:
    sol = next((l[:index] for index, element in enumerate(l) if element > value), l)
    print(sol)
    return sol

def truncate_list(l, value) -> list:
    temp = []
    for element in l:
        temp.append(element)
        if element >= value:
            print(temp)
            return temp
    print(temp)
    return temp


def func1():
    visible_counter = 2*(len(tree_matrix) + len(tree_matrix[0]) - 2)
    for y in range(1, len(tree_matrix) - 1):
        for x in range(1, len(tree_matrix[y]) - 1):
            up = [tree_matrix[y-1-i][x] for i in range(y)]
            down = [tree_matrix[y+1+i][x] for i in range(len(tree_matrix[0])-y-1)]
            left = [tree_matrix[y][x-1-i] for i in range(x)]
            right = [tree_matrix[y][x+1+i] for i in range(len(tree_matrix)-x-1)]
            condition = any(i < tree_matrix[y][x] for i in [max(up), max(down), max(right), max(left)])
            if condition:
                visible_counter += 1
    return visible_counter 
            

def func2():
    scenic_score = []
    for y in range(1, len(tree_matrix) - 1):
        for x in range(1, len(tree_matrix[y]) - 1):
            up = [tree_matrix[y-1-i][x] for i in range(y)]
            down = [tree_matrix[y+1+i][x] for i in range(len(tree_matrix[0])-y-1)]
            left = [tree_matrix[y][x-1-i] for i in range(x)]
            right = [tree_matrix[y][x+1+i] for i in range(len(tree_matrix)-x-1)]
            scenic_score.append(len(truncate_list(up, tree_matrix[y][x])) * len(truncate_list(down, tree_matrix[y][x])) * len(truncate_list(right, tree_matrix[y][x])) * len(truncate_list(left, tree_matrix[y][x])))
    return max(scenic_score)

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')
    stuff = [3]
    print(truncate_list(stuff, 5))