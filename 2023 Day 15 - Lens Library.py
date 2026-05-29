from collections import defaultdict
import re

def hashmap(string):
    val = 0
    for i, ch in enumerate(string):
        val += ord(ch)
        val *= 17
        val %= 256
    return val

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 15 Advent of Code Input.txt"

with open(file) as f:
    sequence = f.readline().strip().split(',')

checksum = 0
for i, lbl in enumerate(sequence):
    val = 0
    for j, ch in enumerate(lbl):
        val += ord(ch)
        val *= 17
        val %= 256
    checksum += val
print(f"Part 1: {checksum}")

boxes = defaultdict(list)
b = 'rn=1'
for i, label in enumerate(sequence):
    m = re.search("=|-", label)
    lbl = label[:m.start()]
    focal_length = label[-1]
    box = hashmap(lbl)
    if '=' in label:
        for j, lens in enumerate(boxes[box]):
            l, f = lens
            if l == lbl:
                boxes[box].pop(j)
                boxes[box].insert(j, (lbl, focal_length))
                break
        else:
            boxes[box].append((lbl, focal_length))
    if '-' in label:
        for j, lens in enumerate(boxes[box]):
            l, f = lens
            if l == lbl:
                boxes[box].pop(j)
                break
focusing_power = sum((box + 1) * (i + 1) * int(lens[1])
                     for box in boxes
                     for i, lens in enumerate(boxes[box]))
print(f"Part 2: {focusing_power}")