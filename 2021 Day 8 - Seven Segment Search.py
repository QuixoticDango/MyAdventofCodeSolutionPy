file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 8 Advent of Code Input.txt"

with open(file) as f:
    maps = []
    for line in f.readlines():
        maps.append((tuple(line.strip().split(' | ')[0].split()), tuple(line.strip().split(' | ')[1].split())))
print(f"Part 1: {sum(1 for inp, out in maps for s in out if len(s) in (2, 3, 4, 7))}")

number_maps = []
segment_maps = [{'t':'', 'tl':'', 'tr':'', 'm':'', 'bl':'', 'br':'', 'b':''}
                for i in range(len(maps))]

inps = tuple(tuple(map(lambda i: set(ch for ch in i), inp)) for inp, out in maps)
outs = tuple(tuple(map(lambda o: set(ch for ch in o), out)) for inp, out in maps)

check = False
output_values = []
for i, inp in enumerate(inps):
    number_maps.append(dict())
    segment_maps.append(dict())
    for j, s in enumerate(inp):
        if len(s) == 7:
            number_maps[i]['8'] = s
        if len(s) == 4:
            number_maps[i]['4'] = s
        if len(s) == 3:
            number_maps[i]['7'] = s
        if len(s) == 2:
            number_maps[i]['1'] = s
    number_maps[i]['2'] = [other for other in inp if len(other) == 5 and
                           set.union(number_maps [i]['4'], other) == number_maps[i]['8']][0]
    number_maps[i]['5'] = [other for other in inp if len(other) == 5 and
                           set.union(number_maps[i]['2'], other) == number_maps[i]['8']][0]
    number_maps[i]['3'] = [other for other in inp if len(other) == 5 and
                           other not in number_maps[i].values()][0]
    number_maps[i]['9'] = [other for other in inp if len(other) == 6 and
                           other == number_maps[i]['5'] | number_maps[i]['3']][0]
    number_maps[i]['6'] = [other for other in inp if len(other) == 6 and
                           other == number_maps[i]['8'].difference(number_maps[i]['1']).union(number_maps[i]['5'])][0]
    number_maps[i]['0'] = [other for other in inp if len(other) == 6 and
                           other != number_maps[i]['6'] and other != number_maps[i]['9']][0]
    segment_maps[i]['t'] = number_maps[i]['7'].difference(number_maps[i]['1']).pop()
    segment_maps[i]['b'] = (number_maps[i]['9'] - number_maps[i]['4'] - set(segment_maps[i]['t'])).pop()
    step = number_maps[i]['5'].copy()
    step.remove(segment_maps[i]['t'])
    step.remove(segment_maps[i]['b'])
    segment_maps[i]['tr'] = (number_maps[i]['4'] - step).pop()
    segment_maps[i]['bl'] = (number_maps[i]['3'] - number_maps[i]['2']).pop()
    segment_maps[i]['m'] = (number_maps[i]['8'] - number_maps[i]['0']).pop()
    segment_maps[i]['br'] = set(l for l in (number_maps[i]['8'] - number_maps[i]['2']) if l in number_maps[i]['1']).pop()
    segment_maps[i]['tl'] = set(l for l in (number_maps[i]['8'] - number_maps[i]['2']) if l not in number_maps[i]['1']).pop()
    number_maps[i] = {frozenset(val):key for key, val in number_maps[i].items()}
    output_values.append(int(''.join(number_maps[i][frozenset(key)] for key in outs[i])))
print(f"Part 2: {sum(output_values)}")

# from collections import defaultdict

# def solve(filename):
#     total_part1 = 0
#     total_part2 = 0

#     with open(filename) as f:
#         for line in f:
#             parts = line.strip().split(" | ")
#             patterns = [set(p) for p in parts[0].split()]
#             outputs = [set(o) for o in parts[1].split()]

#             # Part 1: Count 1, 4, 7, 8 (unique segment counts)
#             total_part1 += sum(1 for o in outputs if len(o) in (2, 3, 4, 7))

#             # Deduce the mapping from pattern to digit
#             digit_map = {}
#             len5 = [p for p in patterns if len(p) == 5]  # candidates for 2, 3, 5
#             len6 = [p for p in patterns if len(p) == 6]  # candidates for 0, 6, 9

#             # Known digits by length
#             one = next(p for p in patterns if len(p) == 2)
#             four = next(p for p in patterns if len(p) == 4)
#             seven = next(p for p in patterns if len(p) == 3)
#             eight = next(p for p in patterns if len(p) == 7)

#             # Find 3: only 5-segment digit that fully contains 1
#             three = next(p for p in len5 if one <= p)
#             len5.remove(three)

#             # Find 9: only 6-segment digit that fully contains 4
#             nine = next(p for p in len6 if four <= p)
#             len6.remove(nine)

#             # Find 0: 6-segment digit that fully contains 1 (the other is 6)
#             zero = next(p for p in len6 if one <= p)
#             len6.remove(zero)
#             six = len6[0]  # last one is 6

#             # Remaining in len5: 2 and 5
#             # 5 is contained within 6 (i.e., 5 ⊆ 6), while 2 is not
#             five = next(p for p in len5 if p <= six)
#             two = next(p for p in len5 if p != five)

#             # Map frozenset(pattern) -> digit
#             mapping = {
#                 frozenset(zero): '0',
#                 frozenset(one): '1',
#                 frozenset(two): '2',
#                 frozenset(three): '3',
#                 frozenset(four): '4',
#                 frozenset(five): '5',
#                 frozenset(six): '6',
#                 frozenset(seven): '7',
#                 frozenset(eight): '8',
#                 frozenset(nine): '9'
#             }

#             # Decode output value
#             output_number = int(''.join(mapping[frozenset(o)] for o in outputs))
#             total_part2 += output_number

#     print(f"Part 1: {total_part1}")
#     print(f"Part 2: {total_part2}")

# # Call the function
# solve(r"C:\Users\lyndo\Documents\Coding and Programming Folder\2021 Day 8 Advent of Code Input.txt")   