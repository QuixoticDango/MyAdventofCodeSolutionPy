file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 9 Advent of Code Input.txt"

def extrapolate_sequence(history: tuple, sequences: list=[]):
    seq = sequences[:]
    if not seq:
        seq.append(history)
    if all(h == 0 for h in history):
        val = 0
        for row in reversed(seq):
            val += row[-1]
        return val
    history = tuple(history[i+1] - h for i, h in enumerate(history) if i+1 < len(history))
    seq.append(history)
    return extrapolate_sequence(history, seq)

def extrapolate_backwards(history: tuple, sequences: list=[]):
    seq = sequences[:]
    if not seq:
        seq.append(history)
    if all(h == 0 for h in history):
        val = 0
        for row in reversed(seq):
            val = row[0] - val
        return val
    history = tuple(history[i+1] - h for i, h in enumerate(history) if i+1 < len(history))
    seq.append(history)
    return extrapolate_backwards(history, seq)

with open(file) as f:
    histories = [tuple(map(int, line.strip().split())) for line in f.readlines()]

print(f"Part 1: {sum(extrapolate_sequence(h) for h in histories)}")
print(f"Part 2: {sum(extrapolate_backwards(h) for h in histories)}")