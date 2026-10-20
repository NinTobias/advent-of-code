from pathlib import Path
from os import path
import re
from functools import reduce
import operator
from itertools import combinations
import numpy as np
from scipy.optimize import linprog

cwd = f'{Path(__file__).parent}\\Inputs\\{path.splitext(path.basename(__file__))[0]}.txt'

with open(cwd, encoding='utf-8') as f:
    lines = [line.rstrip('\n') for line in f] 

def turn_into_binary(line):
    match = re.match(r"^(\[[^\]]+\])\s+((?:\([^)]+\)\s*)+)\s+(\{[^}]+\})$", line)
    if not match:
        return None

    # 1. Parse the Goal State into an integer
    lights_raw = match.group(1).strip("[]")
    num_lights = len(lights_raw)
    
    goal_str = "".join(["1" if char == "#" else "0" for char in lights_raw])
    goal_int = int(goal_str, 2)

    # 2. Parse the Buttons into a list of integers
    middle_part = match.group(2)
    raw_buttons = re.findall(r"\(([^)]+)\)", middle_part)
    
    buttons_int_list = []
    for button in raw_buttons:
        indices = [int(x) for x in button.split(",")]
        button_bits = ["0"] * num_lights
        for idx in indices:
            if idx < num_lights:
                # NO REVERSING: map index directly to the string position
                button_bits[idx] = "1"
        
        buttons_int_list.append(int("".join(button_bits), 2))

    return goal_int, buttons_int_list, num_lights

def xor_n_values_dirty(values : list[int]) -> int:
    total = 0
    for i in range(len(values)):
        total ^= values[i]
    return total

def xor_n_values_clean(values : list[int]) -> int:
    return reduce(operator.xor, values, 0)

def parse_line_b(line):
    match = re.match(r"^(\[[^\]]+\])\s+((?:\([^)]+\)\s*)+)\s+(\{[^}]+\})$", line)
    if not match:
        return None

    # 1. Parse the buttons as lists of affected indices
    middle_part = match.group(2)
    raw_buttons = re.findall(r"\(([^)]+)\)", middle_part)
    buttons = [[int(x) for x in b.split(",")] for b in raw_buttons]

    # 2. Parse the target goals from the curly braces
    last_part = match.group(3).strip("{}")
    goals = [int(x) for x in last_part.split(",")]

    return buttons, goals


def solve_machine_b(buttons, goals):
    num_counters = len(goals)
    num_buttons = len(buttons)
    
    # 1. Build the matrix where columns are button vectors
    # A_eq[r][c] will be 1 if button c affects counter r, else 0
    A_eq = np.zeros((num_counters, num_buttons))
    for c, button in enumerate(buttons):
        for idx in button:
            if idx < num_counters:
                A_eq[idx][c] = 1
                
    # 2. Define the target goals vector
    b_eq = np.array(goals)
    
    # 3. Define the objective function coefficients (we want to minimize the sum: 1·x1 + 1·x2 + ...)
    c = np.ones(num_buttons)
    
    # 4. Define bounds for every variable: each button press must be >= 0
    bounds = [(0, None) for _ in range(num_buttons)]
    
    # 5. Run the Linear Programming solver
    # We use integrality=1 to force the solver to only look for whole-number solutions (MILP)
    result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, 
                     integrality=np.ones(num_buttons))
    
    # If the solver successfully found a valid integer path, return the rounded total presses
    if result.success:
        return int(round(result.fun))
    
    return 0  # Fallback if a machine has no possible mathematical configuration


def func1():
    total = 0
    for line in lines:
        parsed = turn_into_binary(line)
        if not parsed:
            continue
            
        goal_int, buttons, _ = parsed
        
        # We use a nested loop trick: if the inner loop hits 'break', 
        # the 'else' block is SKIPPED. If it finishes without finding anything, 
        # the 'else' block runs and continues the search.
        for i in range(1, len(buttons) + 1):
            for unique_combination in combinations(buttons, i):
                if goal_int == xor_n_values_clean(unique_combination):
                    total += i
                    break  # Breaks the combinations loop
            else:
                continue  # Runs ONLY if no solution was found for this 'i'; moves to next 'i'
            break  # Runs ONLY if the inner loop broke (solution found); moves to next line
            
    return total


def func2():
    total_presses = 0
    for line in lines:
        parsed = parse_line_b(line)
        if parsed:
            buttons, goals = parsed
            res = solve_machine_b(buttons, goals)
            if res != float('inf'):
                total_presses += res
    return total_presses

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')