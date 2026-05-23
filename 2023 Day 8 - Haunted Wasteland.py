from math import lcm

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 8 Advent of Code Input.txt"

# def traverse_nodes(n, steps=0):
#     if n == 'ZZZ':
#         return steps
#     dir = 0 if instructions[steps % len(instructions)] == 'L' else 1
#     next_node = nodes[n][dir]
#     return traverse_nodes(next_node, steps=steps + 1)


with open(file) as f:
    instructions = f.readline().strip()
    _ = f.readline()
    nodes = dict()
    for line in f.readlines():
        parent_node = line[0:3]
        left_child = line[7:10]
        right_child = line[12:15]
        nodes[parent_node] = (left_child, right_child)

# node = 'AAA'
# steps = 0
# while node != 'ZZZ':
#     dir = 0 if instructions[steps % len(instructions)] == 'L' else 1
#     node = nodes[node][dir]
#     steps += 1
# print(f"Part 1: {steps}")

Anodes = [n for n in nodes if n[-1] == 'A']
original = Anodes[:]
factors = [0 for i in range(len(Anodes))]
steps = 0

while not all(n[-1] == 'Z' for n in Anodes):
    if not any(f == 0 for f in factors):
        break
    dir = 0 if instructions[steps % len(instructions)] == 'L' else 1
    for i, n in enumerate(Anodes):
        Anodes[i] = nodes[n][dir]
        if Anodes[i][-1] == 'Z' and factors[i] == 0:
            print('CONDITION')
            print(f"{original[i] = }")
            print(f"{Anodes[i] = }")
            print(f"{nodes[Anodes[i]] = }")
            factors[i] = steps + 1
    steps += 1
print(f"{original[0] = }")
print(f"{Anodes[0] = }")
print(f"{nodes[Anodes[0]] = }") 
print(f"Part 2: {lcm(*factors) = }")
