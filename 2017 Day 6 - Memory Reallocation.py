filename = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2017 Day 6 Advent of Code Input.txt"

with open(filename) as f:
    blocks = list(map(int, f.read().strip().split()))
print(blocks)

seenBlocks = []
seenBlocks.append(blocks)

cycles = 0
while True:
    maxBlock = max(blocks)
    indexOfMax = blocks.index(maxBlock)
    newBlocks = blocks[:]
    newBlocks[indexOfMax] = 0

    count = 1
    while maxBlock > 0:
        newBlocks[(indexOfMax + count) % len(blocks)] += 1
        maxBlock -= 1
        count += 1

    cycles += 1

    if newBlocks in seenBlocks:
        blocks = newBlocks[:]
        break
    
    seenBlocks.append(newBlocks)
    blocks = newBlocks[:]

print(cycles)

seenBlocks2 = []
seenBlocks2.append(blocks)

print(seenBlocks2)
cycles2 = 0
while True:
    maxBlock = max(blocks)
    indexOfMax = blocks.index(maxBlock)
    newBlocks = blocks[:]
    newBlocks[indexOfMax] = 0

    count = 1
    while maxBlock > 0:
        newBlocks[(indexOfMax + count) % len(blocks)] += 1
        maxBlock -= 1
        count += 1

    cycles2 += 1

    if newBlocks in seenBlocks2:
        break
    
    seenBlocks2.append(newBlocks)
    blocks = newBlocks[:]

print(cycles2)