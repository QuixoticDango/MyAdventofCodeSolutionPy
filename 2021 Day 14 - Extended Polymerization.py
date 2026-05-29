from collections import Counter, defaultdict

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 14 Advent of Code Input.txt"

with open(file) as f:
    # chain = [ch for ch in f.readline() if ch != '\n']
    chain = f.readline().strip()
    _ = f.readline()
    rules = {line.split(' -> ')[0]:line.split(' -> ')[1] for line in f.read().splitlines()}

original_chain = chain[:]
steps = 0
while steps < 10:
    # print(chain)
    # print()
    letter_to_ins = []
    slices = []
    for i, ch in enumerate(chain):
        if i+1 < len(chain):
            letter_to_ins.append(rules[ch + chain[i+1]])
            if not slices:
                slices.append(slice(0, i+1, 1))
            else:
                slices.append(slice(slices[-1].stop, i+1, 1))
    new_chain = ''
    for i, sl in enumerate(slices):
        new_chain += chain[sl] + letter_to_ins[i]
    else:
        new_chain += chain[slices[-1].stop:]
    chain = new_chain
    steps += 1

count = Counter(chain)
print(f"Part 1: {max(count.values()) - min(count.values())}")


# Partially failed Part 2.
chain = original_chain
pair_counts = {k:0 for k in rules}
already_present = {}
for i, ch in enumerate(chain):
    if i+1 < len(chain):
        pair_counts[ch + chain[i+1]] += 1

for _ in range(40):
    new_pairs = defaultdict(int)
    for pair, count in pair_counts.items():
        if pair in rules:
            c = rules[pair]
            new_pairs[pair[0] + c] += count
            new_pairs[c + pair[1]] += count
    pair_counts = new_pairs
    # steps += 1
elements = {ch:0 for ch in (c for k in pair_counts for c in k)}
for k, v in pair_counts.items():
    elements[k[0]] += v
elements[chain[-1]] += 1
print(f"Part 2: {max(elements.values()) - min(elements.values())}")