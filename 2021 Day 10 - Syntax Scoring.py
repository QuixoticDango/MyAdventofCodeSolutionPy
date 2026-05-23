
file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 10 Advent of Code Input.txt"

with open(file) as f:
    lines = f.read().splitlines()

sym_map = dict(zip("({[<", ")}]>"))
score = dict(zip(")]}>", [3, 57, 1197, 25137]))
s = 0
corrupted = set()
for i, row in enumerate(lines):
    symbol = []
    for j, ch in enumerate(row):
        if ch in "[{(<":
            symbol.append(ch)
        if ch in "]})>":
            if ch != sym_map[symbol[-1]] or not sym_map:
                s += score[ch]
                corrupted.add(row)
                break
            if ch == sym_map[symbol[-1]]:
                symbol.pop()           
print(f"Part 1: {s}")

score = dict(zip("([{<", [1, 2, 3, 4]))
scores = []
for i, row in enumerate(line for line in lines if line not in corrupted):
    s = 0
    symbol = []
    for j, ch in enumerate(row):
        if ch in "[{(<":
            symbol.append(ch)
        if ch in "]})>":
            # if ch != sym_map[symbol[-1]] or not sym_map:
            #     s += score[ch]
            #     corrupted.add(row)
            #     break
            if ch == sym_map[symbol[-1]]:
                symbol.pop()
    for ch in reversed(symbol):
        s = 5 * s + score[ch]
    scores.append(s)
print(len(scores))
print(f"Part 2: {sorted(scores)[len(scores) // 2]}")