file = "C:\\Users\\DANGO\\Documents\\Coding and Programming Folder\\2025 Day 3 Advent of Code Input.txt"

with open(file, 'rt') as f:
    banks = [line.strip() for line in f.readlines()]

total_joltage = 0
for bank in banks:
    max_digit_loc = [tup for tup in enumerate(bank) if int(tup[1]) == max(int(digit) for digit in bank)][0]
    if max_digit_loc[0] == len(bank) - 1:
        total_joltage += int([digit for digit in bank[:-1] 
                              if int(digit) == max(int(d) for d in bank[:-1])][0] + max_digit_loc[1])
    else:
        total_joltage += int(max_digit_loc[1] + [digit for digit in bank[max_digit_loc[0] + 1:] 
                                                 if int(digit) == max(int(d) for d in bank[max_digit_loc[0] + 1:])][0])
print(total_joltage)
