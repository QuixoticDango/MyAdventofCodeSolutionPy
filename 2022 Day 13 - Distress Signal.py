file: str = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2022 Day 13 Advent of Code Input.txt"

with open(file) as f:
    packet_pairs: list[list[list[int | list], list[int | list]]]= []
    pair: list = []
    for line in f.readlines():
        if line == '\n':
            packet_pairs.append(pair)
            pair = []
        else:
            pair.append(eval(line.strip()))
    else:
        packet_pairs.append(pair)

# try making a function for comparing members of a list
count = 0
for i, [left, right] in enumerate(packet_pairs):
    for j, l in left:
        try:
            if l > right[j]:
                continue
        except TypeError:
            if type(l) == list:
                for k, n in l:
                    if 