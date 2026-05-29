file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 7 Advent of Code Input.txt"

with open(file) as f:
    starting_pos = tuple(map(int, f.readline().strip().split(',')))

def fuel_cost(final_pos: int) -> int:
    return sum(abs(final_pos - init_pos) for init_pos in starting_pos)
def inc_fuel_cost(final_pos: int) -> int:
    return sum(abs(final_pos - init_pos) * (abs(final_pos - init_pos) + 1) // 2
               for init_pos in starting_pos)
print(f"Part 1: {min(fuel_cost(i) for i in range(min(starting_pos), max(starting_pos) + 1))}")
print(f"Part 2: {min(inc_fuel_cost(i) for i in range(min(starting_pos), max(starting_pos) + 1))}")