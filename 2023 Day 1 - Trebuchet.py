file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 1 Advent of Code Input.txt"

with open(file, 'rt') as f:
    calibration_values = [line.strip() for line in f.readlines()]

actual_values = []
for line in calibration_values:
    value = ''
    for ch in line:
        if ch.isnumeric():
            value += ch
            break
    for i in range(len(line) - 1, -1, -1):
        if line[i].isnumeric():
            value += line[i]
            break
    actual_values.append(int(value))

print(sum(actual_values))

# Part 2

import re

def locate_number(cal_val):
    index = []
    value = ''
    for i, ch in enumerate(cal_val):
        if ch.isnumeric():
            index.append((i, ch))
            break
        
    pattern = re.compile("|".join(number_words))
    m = re.search(pattern, cal_val)
    try:
        if m.start() < index[0][0]:
            num_word = cal_val[m.start():m.end()]
            value += num_dict[num_word]
        else:
            value += index[0][1]
    except AttributeError:
        value += index[0][1]
    except IndexError:
        num_word = cal_val[m.start():m.end()]
        value += num_dict[num_word]
    
    reversed_nums = [''.join([num[i] for i in range(-1, -len(num) - 1, -1)]) for num in number_words]
    reversed_cal_val = ''.join([cal_val[i] for i in range(-1, -len(cal_val) - 1, -1)])
    reversed_num_dict = dict(zip(reversed_nums, digits))
    pattern = re.compile('|'.join(reversed_nums))
    m = re.search(pattern, reversed_cal_val)

    index = []
    for i, ch in enumerate(reversed_cal_val):
        if ch.isnumeric():
            index.append((i, ch))
            break

    try:
        if m.start() < index[0][0]:
            num_word = reversed_cal_val[m.start():m.end()]
            value += reversed_num_dict[num_word]
        else:
            value += index[0][1]
    except AttributeError:
        value += index[0][1]
    except IndexError:
        num_word = reversed_cal_val[m.start():m.end()]
        value += reversed_num_dict[num_word]
    
    return int(value)

number_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
pattern = re.compile("|".join(number_words))
digits = list(map(str, range(1, 10)))
num_dict = dict(zip(number_words, digits))

print(sum(locate_number(cal) for cal in calibration_values))