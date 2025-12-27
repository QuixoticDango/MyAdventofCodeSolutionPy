from itertools import product

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2019 Day 2 Advent of Code Input.txt"

def run_intcode(noun, verb, lst):
    d = lst.copy()
    d[1] = noun
    d[2] = verb

    for i in range(0, len(d), 4):
        if d[i] == 99:
            break
        if d[i] == 1:
            d[d[i+3]] = d[d[i+1]] + d[d[i+2]]
        if d[i] == 2:
            d[d[i+3]] = d[d[i+1]] * d[d[i+2]]
        if not (d[i] == 1 or d[i] == 2 or d[i] == 99):
            print(d[i])
            break
    return d[0]

with open(file) as f:
    raw = f.read().strip().split(',')
    data = [int(r) for r in raw]
    
# data[1] = 12
# data[2] = 2
# intcode = data

# for i in range(0, len(data), 4):
#     if data[i] == 99:
#         break
#     if data[i] == 1:
#         data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
#     if data[i] == 2:
#         data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
#     if not (data[i] == 1 or data[i] == 2 or data[i] == 99):
#         print(data[i])
#         break

# print(data[0])

for noun, verb in product(range(0,100), range(0,100)):
    if run_intcode(noun, verb, data) == 19690720:
        print(100 * noun + verb)