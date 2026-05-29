def scenic_score(grid: list[str], loc: tuple[int, int]) -> int:
    i, j = loc
    up: int = 0
    down: int = 0
    left: int = 0
    right: int = 0

    for c in range(j-1, -1, -1):
        if grid[i][c] < grid[i][j]:
            left += 1
        else:
            left += 1
            break
    
    for c in range(j+1, len(grid[i])):
        if grid[i][c] < grid[i][j]:
            right += 1
        else:
            right += 1
            break

    for r in range(i-1, -1, -1):
        if grid[r][j] < grid[i][j]:
            up += 1
        else:
            up += 1
            break
    
    for r in range(i+1, len(grid)):
        if grid[r][j] < grid[i][j]:
            down += 1
        else:
            down += 1
            break

    return up * down * left * right

file: str = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2022 Day 8 Advent of Code Input.txt"

with open(file) as f:
    forest: list[str] = f.read().splitlines()

visible_trees: int = 0

for i, row in enumerate(forest):
    for j, tree in enumerate(row):
        # Tree is on the perimeter
        if i == 0 or i == len(forest) - 1 or j == 0 or j == len(forest) - 1:
            visible_trees += 1
            continue
        
        if all(row[k] < tree for k in range(j)):
            visible_trees += 1
            continue
        if all(row[k] < tree for k in range(-1, j - len(row), -1)):
            visible_trees += 1
            continue
        if all(forest[k][j] < tree for k in range(i)):
            visible_trees += 1
            continue
        if all(forest[k][j] < tree for k in range(-1, i - len(forest), -1)):
            visible_trees += 1

print(f"Part 1: {visible_trees}")

best_scenic_score = max(scenic_score(forest, (i,j))
                        for i in range(len(forest))
                        for j in range(len(forest[i])))

print(f"Part 2: {best_scenic_score}")