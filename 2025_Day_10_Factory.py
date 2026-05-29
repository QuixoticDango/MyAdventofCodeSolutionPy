from itertools import combinations, product, count
import numpy as np

file = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2025 Day 10 Advent of Code Input.txt"

with open(file, 'rt') as f:
    raw = [line.strip().split() for line in f.readlines()]

solutions = []
button_lsts = []
joltage_values = []
for line in raw:
    button_count = sum(1 for t in line if '(' in t)
    buttons = []
    for item in line:
        if ']' in item:
            solution = [1 if ch == '#' else 0 for i, ch in enumerate(item[1:-1])]
            solutions.append(np.array(solution).transpose())
            continue
        if '(' in item:
            button = list(map(int, item[1:-1].split(',')))
            state = np.array([1 if i in button else 0 for i in range(len(solution))])
            buttons.append(state)
            continue
        if '}' in item:
            joltages = tuple(map(int, item[1:-1].split(',')))
        button_lsts.append(buttons)
        joltage_values.append(joltages)

# s = 0
# for i, solution in enumerate(solutions):
#     found_solution = False
#     for j in range(1, len(button_lsts[i])):
#         if found_solution:
#             break
#         for buttons in combinations(button_lsts[i], j):
#             state = sum(buttons[k] for k in range(j)) % 2
#             print(f"{state=}")
#             if all(state[l] == solution[l] for l in range(len(state))):
#                 found_solution = True
#                 s += j
#                 break
# print(s)
s = 0
joltage_values = [np.array(j) for j in joltage_values]
print(all(len(button_lsts[i]) >= len(joltage_values[i]) for i in range(len(button_lsts))))
r = 0
for i in range(len(button_lsts)):
    if len(button_lsts[i]) == len(joltage_values[i]):
        try:
            # print(f"Buttons: {button_lsts[i]} | Joltages: {joltage_values[i]}")
            print(np.linalg.solve((np.array(button_lsts[i])).transpose(), joltage_values[i]))
            print()
        except np.linalg.LinAlgError as e:
            print(f'ERROR: {e.args[0]}')
            print(f"Buttons: {button_lsts[i]} | Joltages: {joltage_values[i]}")
            print()
            error_found = True
        # while error_found:
            found = False
            for j, b1 in enumerate(button_lsts[i]):
                # print('MADE IT TO FIRST FOR LOOP')
                if found:
                    break
                for c in range(2, len(button_lsts[i]) - 1):
                    if found:
                        break
                    for combo in combinations([b2 for k, b2 in enumerate(button_lsts[i]) if j != k], c):
                        if all(b1[m] == sum(combo)[m] % 2 for m in range(len(b1))):
                            print(f"{b1} is a linear combination of {combo}")
                            print()
                            print(f"All buttons: {button_lsts[i]}")
                            del button_lsts[i][j]
                            print(f"{b1} has been deleted. Buttons: {button_lsts[i]}")
                            found = True
                            break
                # try:
                #     print(f"Second solution attempt: {np.linalg.solve(button_lsts[i], joltage_values[i])}")
                #     print()
                #     error_found = False
                # except np.linalg.LinAlgError as e:
                #     print(f"Error found again: {e.args[0]}")
                #     print(f"Current buttons: {button_lsts[i]}")
                #     # if not any(b == sum(combo)[v] % 2 
                #     #            for w, b in enumerate(buttons))
                #     error_found = True


        r += 1
print(f"Count: {r}")
print(f"Total: {len(button_lsts)}")

a = np.array([[1,1,1,1,1], [0,1,0,1,0], [1,0,1,1,0], [1,0,0,1,0], [1,0,1,1,1]]).transpose()
for row in a:
    print(row)

# b = np.array([201,30,21,221,10])
# print(sum(np.linalg.solve(a, b)))
# # # print(f"{joltage_values[0]=}")
# # for i, jolt in enumerate(joltage_values):
#     # print(f"{joltages=}")
#     found_solution = False
#     for j in count(max(jolt), 1):
#         # print(f"{j=}")
#         if found_solution:
#             break
#         for buttons in product(button_lsts[i], repeat=j):
#             # print(f"{buttons=}")
#             state = sum(buttons[k] for k in range(j))
#             state = list(state)
#             jolt = list(jolt)
#             # print(f"{list(state)=}")
#             # print(f"{joltage_values[0]=}")
#             if all(state[l] == jolt[l] for l in range(len(state))):
#                 found_solution = True
#                 s += j
#                 break
# print(s)