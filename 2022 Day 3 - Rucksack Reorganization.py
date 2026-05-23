file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2022 Day 3 Advent of Code Input.txt"

with open(file) as f:
    data: list[str] = f.read().splitlines()
    letters: str = 'abcdefghijklmnopqrstuvwxyz'
    letters += ''.join(ch.upper() for ch in letters)
    priority: dict = dict(zip(letters, [i for i in range(1, len(letters) + 1)]))
    score: int = 0
    score_2: int = 0
    elves: list = []

    for line in data:
        # Part 1
        first = set(ch for ch in line[:len(line) // 2])
        second = set(ch for ch in line[len(line) // 2:])
        score += priority[(first & second).pop()]

        # Part 1
        elves.append(set(ch for ch in line))
        if len(elves) == 3:
            score_2 += priority[set.intersection(*elves).pop()]
            elves = []

print(f"Part 1: {score}")
print(f"Part 2: {score_2}")