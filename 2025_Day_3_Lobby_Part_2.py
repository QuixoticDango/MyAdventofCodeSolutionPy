file = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2025 Day 3 Advent of Code Input.txt"

with open(file, 'rt') as f:
    banks = [line.strip() for line in f.readlines()]
    
total_joltage = 0
for bank in banks:
    max_digits = ""
    for c in range(12):
        if c == 11:
            max_digit_loc = [tup for tup in enumerate(bank) if int(tup[1]) == max(int(digit) for digit in bank)][0]
        else:
            max_digit_loc = [tup for tup in enumerate(bank[:-11 + c]) if int(tup[1]) == max(int(digit) for digit in bank[:-11 + c])][0]
        
        max_digits += max_digit_loc[1]
        bank = bank[max_digit_loc[0] + 1:]

    total_joltage += int(max_digits)
print(total_joltage)
