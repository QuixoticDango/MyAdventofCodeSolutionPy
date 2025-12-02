def isPrime(n):
    if n == 2:
        return True
    if n < 2:
        return False
    if any(n % i == 0 for i in range(2, int(n**0.5) + 1)):
        return False
    return True
file = "C:\\Users\\DANGO\\Documents\\Coding and Programming Folder\\2025 Day 2 Advent of Code Input.txt"

with open(file, 'rt') as f:
    ranges = f.readline().strip().split(',')
    ranges = [list(map(int, r.split('-'))) for r in ranges]
    ranges = [tuple(map(str, (i for i in range(a, b+1)))) for a, b in ranges]
    
s=0
for r in ranges:
    for num_str in r:
        if isPrime(len(num_str)):
            if all(num_str[i] == num_str[j] for i in range(len(num_str)) for j in range(len(num_str)) if i != j):
                s += int(num_str)
                continue

        factors = [i for i in range(1, len(num_str) // 2 + 1) if len(num_str) % i == 0]
        for f in factors:
            if all(num_str[i*f:(i+1)*f] == num_str[(i+1)*f:(i+2)*f] for i in range(len(num_str) // f - 1)):
                s += int(num_str)
                break
print(f"{s=}")
