import re
from collections import defaultdict

def reduce_number(num: str) -> str:
    i = 0
    idx = 0
    depth = 0
    while i < len(num):
        ch = num[i]
        if ch == '[':
            depth += 1
        if ch == ']':
            depth -= 1
        if ch.isnumeric():
            if depth > 4:
                # Explode
                if (idx+1, depth) in p_dct:
                    try:
                        new_num_left = p_dct[num_locs.index((idx,depth))-1] + int(ch)
                    except IndexError:
                        new_num_left = None
                    try:
                        new_num_right = p_dct[num_locs.index((idx,depth))+1] + p_dct[num_locs.index((idx,depth))+2]
                    except IndexError:
                        new_num_right = None
                    if new_num_left:
                        
            idx += 1
        i += 1
file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 18 Advent of Code Input.txt"

with open(file) as f:
    problem = []
    for line in map(eval, f.read().splitlines()):
        problem += [line]
problem = [problem]
problem = ','.join(str(p) for p in problem).replace(' ', '')
print(re.findall(r"\d+", problem))
# organized_problem = []
# p_lst = []
p_dct = {}
depth = 0
idx = 0
i = 0
while i < len(problem):
    ch = problem[i]
# for idx, ch in enumerate(problem):
    if ch == '[':
        depth += 1
    if ch == ']':
        depth -= 1
    if ch.isnumeric():
        # p_lst.append((int(ch), (idx, depth)))
        p_dct[(idx, depth)] = int(ch)
        idx += 1
    i += 1
num_locs = sorted(p_dct, key=lambda s: s[0])
print(p_dct)

# num_locs = sorted(p_dct, key=lambda s: s[0])
# for i, (idx, d) in enumerate(num_locs):
#     if i + 1 < len(num_locs):
#         if num_locs[i+1][0] - num_locs[i][0] == 1 and num_locs[i+1][1] == num_locs[i][1]:
#             print(num_locs[i], num_locs[i+1])
#     if num_locs[i][1] > 4:
#         print('FOUND ONE')

    # if i > 0 and depth == 0:
    #     organized_problem.append(p_lst)
    #     # check = True
    #     break
# print(organized_problems)
# for i, problem in enumerate(organized_problem):
#     for j, (num, depth) in enumerate(problem):
#         if depth >= 4:
#             print(depth)