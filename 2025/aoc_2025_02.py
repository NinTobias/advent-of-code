from pathlib import Path

cwd = Path(__file__).parent / "Inputs" / f"{Path(__file__).stem}.txt"

with open(cwd, encoding="utf-8") as f:
    lines = f.read().split(",")

def has_repeating_subsequence(s : str) -> bool:
    """Function to check if a number consists only of a subsequnce that repeats exactly twice.
    For example, 1212 is a repeating subsequence of 12, but 1234 is not a repeating subsequence."""
    front_half, back_half = s[:len(s)//2], s[len(s)//2:]
    return front_half == back_half

def has_multiple_repeating_subsequences(s : str) -> bool:
    """Function to check if a number consists of multiple subsequences that repeat however many times.
    For example, 121212 is a repeating subsequence of 12, but 1234 is not a repeating subsequence."""
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            subseq = s[:i]
            if subseq * (n // i) == s:
                return True
    return False

def func1():
    total = 0
    for line in lines:
        first, last = line.split("-")
        for i in range(int(first), int(last) + 1):
            if has_repeating_subsequence(str(i)):
                #print(f'Found invalid ID: {i}')
                total += i
    return total

def func2():
    total = 0
    for line in lines:
        first, last = line.split("-")
        for i in range(int(first), int(last) + 1):
            if has_multiple_repeating_subsequences(str(i)):
                #print(f'Found invalid ID: {i}')
                total += i
    return total    

if __name__ == '__main__':
    print(f'Solution Part A: {func1()}')
    print(f'Solution Part B: {func2()}')