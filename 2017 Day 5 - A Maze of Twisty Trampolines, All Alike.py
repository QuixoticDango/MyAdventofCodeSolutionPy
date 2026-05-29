filename = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2017 Day 5 Advent of Code Input.txt"

with open(filename) as f:
    jumps = [int(num.strip()) for num in f.readlines()]

def stepsToExit(jumps):
    start_position = 0
    new_position = 0
    steps = 0
    while 0 <= new_position < len(jumps):
            new_position = start_position + jumps[start_position]
            jumps[start_position] += 1
            start_position = new_position
            steps += 1

    print(f"Final: {new_position}")
    print(steps)

def stepsToExit2(jumps):
    start_position = 0
    new_position = 0
    steps = 0
    while 0 <= new_position < len(jumps):
            new_position = start_position + jumps[start_position]
            if jumps[start_position] >= 3:
                jumps[start_position] -= 1
            else:
                jumps[start_position] += 1
            start_position = new_position
            steps += 1

    print(f"Final: {new_position}")
    print(steps)

stepsToExit2(jumps)