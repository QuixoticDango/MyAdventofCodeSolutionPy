file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2020 Day 6 Advent of Code Input.txt"

with open(file) as f:
    groups = []
    answers = set()
    all_lines = [line for line in f.readlines()]

for line in all_lines:
    if line == '\n':
        groups.append(answers)
        answers = set()
        continue
    for ch in line.strip():
        answers.add(ch)
else:
    groups.append(answers)

print(f"Part 1: {sum(len(g) for g in groups)}")

groups = []
all_people_in_group = []
for i, line in enumerate(all_lines):
    if line == '\n':
        groups.append(set.intersection(*all_people_in_group))
        all_people_in_group = []
        continue
    person = {ch for ch in line.strip()}
    all_people_in_group.append(person.copy())
else:
    groups.append(set.intersection(*all_people_in_group))

print(f"Part 2: {sum(len(g) for g in groups)}")