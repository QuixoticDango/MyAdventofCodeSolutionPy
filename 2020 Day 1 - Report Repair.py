file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2020 Day 1 Advent of Code Input.txt"

with open(file) as f:
    nums = [int(line.strip()) for line in f.readlines()]

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == 2020:
            print(f"Part 1: {nums[i] * nums[j]}")

for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            if nums[i] + nums[j] + nums[k] == 2020:
                print(f"Part 2: {nums[i] * nums[j] * nums[k]}")