from functools import cache
from tqdm import tqdm

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 12 Advent of Code Input.txt"

with open(file) as f:
    input = f.read().splitlines()
print(input)

@cache
def count_arrangements(conditions, rules):
    if not rules:
        return 0 if "#" in conditions else 1
    if not conditions:
        return 1 if not rules else 0
    
    result = 0

    if conditions[0] in ".?":
        result += count_arrangements(conditions[1:], rules)
    if conditions[0] in "#?":
        if (
            rules[0] <= len(conditions)
            and "." not in conditions[:rules[0]]
            and (rules[0] == len(conditions) or conditions[rules[0]] != '#')
        ):
            result += count_arrangements(conditions[rules[0] + 1:], rules[1:])
    return result

solution1 = 0
solution2 = 0
for line in input:
    conditions, rules = line.split()
    rules = eval(rules)
    solution1 += count_arrangements(conditions, rules)

    conditions = "?".join([conditions] * 5)
    rules = rules * 5
    solution2 += count_arrangements(conditions, rules)

print("Solution 1:", solution1)
print(f"Solution 2: {solution2:,}")