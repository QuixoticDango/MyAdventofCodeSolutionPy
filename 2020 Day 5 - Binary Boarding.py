def partition(inst: str, remaining_rows: list = None, remaining_columns: list = None, runs: int = 0) -> int:
    # print(f"{runs = }")
    if runs == 0:
        remaining_rows = [i for i in range(128)]
        remaining_columns = [j for j in range(8)]
    # print(f"{remaining_rows = }")
    if not inst:
        # print('return')
        return remaining_rows[0] * 8 + remaining_columns[0]
    
    # if len(remaining_seats) == 1:
    #     remaining_seats = remaining_seats[0]
    #     print(f"{remaining_seats = }")
    
    if inst[0] == 'F':
        # print("F")
        return partition(inst[1:], remaining_rows[:len(remaining_rows) // 2], remaining_columns, runs = runs + 1)
    
    if inst[0] == 'B':
        # print("B")
        return partition(inst[1:], remaining_rows[len(remaining_rows) // 2:], remaining_columns, runs = runs + 1)
    
    if inst[0] == 'L':
        # print('L')
        return partition(inst[1:], remaining_rows, remaining_columns[:len(remaining_columns) // 2], runs = runs + 1)
    
    if inst[0] == 'R':
        # print('R')
        return partition(inst[1:], remaining_rows, remaining_columns[len(remaining_columns) // 2:], runs = runs + 1)

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2020 Day 5 Advent of Code Input.txt"

with open(file) as f:
    instructions = [line.strip() for line in f.readlines()]

print(f"Part 1: {max(partition(instruction) for instruction in instructions)}")

# Part 2
seat_IDs = [partition(i) for i in instructions]

for i in range(856):
    if (i + 1) in seat_IDs and (i - 1) in seat_IDs and i not in seat_IDs:
        print(f"Part 2: {i}")