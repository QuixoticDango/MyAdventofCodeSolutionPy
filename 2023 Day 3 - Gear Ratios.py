from itertools import product

class NegativeIndex(IndexError):
    pass

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 3 Advent of Code Input.txt"

with open(file, 'rt') as f:
    grid = [line.strip() for line in f.readlines()]

# print(grid)
directions = list(product([-1, 0, 1], repeat=2))
del directions[directions.index((0,0))]

found_symbol = False
part_numbers = []
for r, row in enumerate(grid):
    value = ''
    for c, ch in enumerate(row):
        if ch.isnumeric():
            value += ch
            if not found_symbol:
                for d in directions:
                    try:
                        if r + d[0] < 0 or c + d[1] < 0:
                            raise NegativeIndex
                        if not (grid[r + d[0]][c + d[1]] == '.' \
                            or grid[r + d[0]][c + d[1]].isnumeric()):
                            found_symbol = True
                    except NegativeIndex:
                        pass
                    except IndexError:
                        pass
        if not ch.isnumeric() or c == len(row) - 1:
            if found_symbol:
                part_numbers.append(int(value))
                value = ''
                found_symbol = False
            else:
                value = ''
print(sum(part_numbers))

found_gear = False
gear_ratios = dict()
gear_list = []
for r, row in enumerate(grid):
    value = ''
    for c, ch in enumerate(row):
        if ch.isnumeric():
            value += ch
            if not found_gear:
                for d in directions:
                    try:
                        if r + d[0] < 0 or c + d[1] < 0:
                            raise NegativeIndex
                        if grid[r + d[0]][c + d[1]] == '*':
                            gear_list.append((r + d[0], c + d[1]))
                            found_gear = True
                    except NegativeIndex:
                        pass
                    except IndexError:
                        pass
        if not ch.isnumeric() or c == len(row) - 1:
            if found_gear:
                if int(value) not in gear_ratios.keys():
                    gear_ratios[int(value)] = gear_list
                else:
                    gear_ratios[int(value)] += gear_list
                value = ''
                gear_list = []
                found_gear = False
            else:
                gear_list = []
                value = ''

gears = set()
for key in gear_ratios.keys():
    for g in gear_ratios[key]:
        gears.add(g)

sum_of_ratios = 0
for g in gears:
    # gear_count = 0
    gear_pairs = []
    for key in gear_ratios.keys():
        if g in gear_ratios[key]:
            # gear_count += 1
            gear_pairs.append(key)
    if len(gear_pairs) == 2:
        sum_of_ratios += gear_pairs[0] * gear_pairs[1]

print(sum_of_ratios)