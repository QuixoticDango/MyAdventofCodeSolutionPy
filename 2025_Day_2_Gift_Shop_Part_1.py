file = "C:\\Users\\DANGO\\Documents\\Coding and Programming Folder\\2025 Day 2 Advent of Code Input.txt" # <-- This should be whatever file you have your prompt stored in.  

with open(file, 'rt') as f:
    ranges = f.readline().strip().split(',')
    ranges = [list(map(int, r.split('-'))) for r in ranges]
    ranges = [tuple(map(str, (i for i in range(a, b+1)))) for a, b in ranges]

s = sum(int(num_str) for r in ranges for num_str in r 
        if len(num_str) % 2 == 0 and num_str[:len(num_str) // 2] == num_str[len(num_str) // 2:])
print(s)
