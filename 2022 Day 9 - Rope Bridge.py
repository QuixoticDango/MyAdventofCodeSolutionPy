from itertools import product
from collections.abc import Sequence

def tail_is_touching(hpos: tuple[int, int], tpos: tuple[int, int]) -> bool:
    dir: Sequence[Sequence[int]] = list(product([-1,0,1], repeat=2))
    if any((hpos[0] + di, hpos[1] + dj) == tpos for di, dj in dir):
        return True
    return False

file: str = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2022 Day 9 Advent of Code Input.txt"

with open(file) as f:
    instructions: list = list(map(lambda l: l.split(), f.read().splitlines()))
    instructions = [(d, int(n)) for d, n in instructions]

visited: set = set()
curr_hpos: tuple[int, int] = 0,0
curr_tpos: tuple[int, int] = 0,0

for d, n in instructions:
    steps: int = 0
    if d == "L":
        while steps < n:
            curr_hpos = (curr_hpos[0], curr_hpos[1] - 1)
            if not tail_is_touching(curr_hpos, curr_tpos):
                curr_tpos = (curr_hpos[0], curr_hpos[1] + 1)
                visited.add(curr_tpos)
            steps += 1
    if d == "R":
        while steps < n:
            curr_hpos = (curr_hpos[0], curr_hpos[1] + 1)
            if not tail_is_touching(curr_hpos, curr_tpos):
                curr_tpos = (curr_hpos[0], curr_hpos[1] - 1)
                visited.add(curr_tpos)
            steps += 1
    if d == "U":
        while steps < n:
            curr_hpos = (curr_hpos[0] - 1, curr_hpos[1])
            if not tail_is_touching(curr_hpos, curr_tpos):
                curr_tpos = (curr_hpos[0] + 1, curr_hpos[1])
                visited.add(curr_tpos)
            steps += 1
    if d == "D":
        while steps < n:
            curr_hpos = (curr_hpos[0] + 1, curr_hpos[1])
            if not tail_is_touching(curr_hpos, curr_tpos):
                curr_tpos = (curr_hpos[0] - 1, curr_hpos[1])
                visited.add(curr_tpos)
            steps += 1
print(f"Part 1: {len(visited)}")

visited = set()
curr_positions: dict[str|int, tuple[int, int]] = {i:(0,0) for i in range(10)}
visited.add((0,0))

for d, n in instructions:
    steps: int = 0
    if d == "L":
        while steps < n:
            curr_positions[0] = (curr_positions[0][0], curr_positions[0][1] - 1)
            for i in range(10):
                if i+1 < len(curr_positions):
                    if not tail_is_touching(curr_positions[i], curr_positions[i+1]):
                        curr_positions[i+1] = (curr_positions[i][0], curr_positions[i][1] + 1)
                        if i+1 == 9:
                            visited.add(curr_positions[i+1])
            steps += 1
    if d == "R":
        while steps < n:
            curr_positions[0] = (curr_positions[0][0], curr_positions[0][1] + 1)
            for i in range(10):
                if i+1 < len(curr_positions):
                    if not tail_is_touching(curr_positions[i], curr_positions[i+1]):
                        curr_positions[i+1] = (curr_positions[i][0], curr_positions[i][1] - 1)
                        if i+1 == 9:
                            visited.add(curr_positions[i+1])
            steps += 1
    if d == "U":
        while steps < n:
            curr_positions[0] = (curr_positions[0][0] - 1, curr_positions[0][1])
            for i in range(10):
                if i+1 < len(curr_positions):
                    if not tail_is_touching(curr_positions[i], curr_positions[i+1]):
                        curr_positions[i+1] = (curr_positions[i][0] + 1, curr_positions[i][1])
                        if i+1 == 9:
                            visited.add(curr_positions[i+1])
            steps += 1
    if d == "D":
        while steps < n:
            curr_positions[0] = (curr_positions[0][0] + 1, curr_positions[0][1])
            for i in range(10):
                if i+1 < len(curr_positions):
                    if not tail_is_touching(curr_positions[i], curr_positions[i+1]):
                        curr_positions[i+1] = (curr_positions[i][0] - 1, curr_positions[i][1])
                        if i+1 == 9:
                            visited.add(curr_positions[i+1])
            steps += 1
print(f"Part 2: {len(visited)}")