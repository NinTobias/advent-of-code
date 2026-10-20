from pathlib import Path
from os import path
import re

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd, encoding='utf-8') as f:
    lines = [line.rstrip('\n') for line in f]
    sanitized_data = []
    for line in lines:
        match = re.match(r"^([a-z]+):\s+(.+)$", line)
        if match:
            key = match.group(1)
            # Split the remaining string by spaces to get individual values
            values = match.group(2).split()
            
            sanitized_data.append([key, values])
    
lookup = dict(sanitized_data)

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def __repr__(self):
        child_names = [child.name for child in self.children]
        return f"{self.name} -> {child_names}"
    

def build_tree(node_name):
    node = TreeNode(node_name)   
    # If this node has children listed in our data, build them too
    if node_name in lookup:
        for child_name in lookup[node_name]:
            node.children.append(build_tree(child_name))
            
    return node

def find_all_paths(graph, start, target):
    all_paths = []
    
    # The stack stores tuples of: (current_node, [path_taken_to_get_here])
    stack = [(start, [start])]
    
    while stack:
        current_node, current_path = stack.pop()
        
        # If we reached the target, save this completed path
        if current_node == target:
            all_paths.append(current_path)
            continue
            
        # If the node has children, explore them
        if current_node in graph:
            # Reversing the list keeps the paths in left-to-right order, 
            # though it's optional!
            for neighbor in reversed(graph[current_node]):
                stack.append((neighbor, current_path + [neighbor]))
                
    return all_paths 


def func1():
    paths = find_all_paths(lookup, "you", "out")

    print(f"Found {len(paths)} unique paths:")
    for p in paths:
        print(" -> ".join(p))

    return(len(paths))


def func2():
    paths = find_all_paths(lookup, "svr", "dac")

    #required_nodes = {"dac", "fft"}

    #paths = [path for path in paths if required_nodes.issubset(path)]

    print(f"Found {len(paths)} unique paths:")
    for p in paths:
        print(" -> ".join(p))

    return(len(paths))


if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')