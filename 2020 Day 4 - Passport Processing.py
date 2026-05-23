import re

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2020 Day 4 Advent of Code Input.txt"

def is_valid(p: dict) -> bool:
    if len(p) < 7:
        return False
    if len(p) == 7 and "cid" in p:
        return False
    if len(p) == 7 and "cid" not in p:
        return True
    if len(p) == 8:
        return True
    
def valid_fields(p: dict) -> bool:
    if not is_valid(p):
        return False

    for key in p:
        if key == 'byr':
            if p['byr'] > '2002' or p['byr'] < '1920' or len(p['byr']) != 4:
                return False
        if key == 'iyr':
            if p['iyr'] > '2020' or p['iyr'] < '2010' or len(p['iyr']) != 4:
                return False
        if key == 'eyr':
            if p['eyr'] > '2030' or p['eyr'] < '2020' or len(p['eyr']) != 4:
                return False
        if key == 'hgt':
            m = re.search("\d+cm|\d+in", p['hgt'])

            if m == None:
                return False
            
            sl = slice(m.start(), m.end())
            height = p['hgt'][sl]

            if p['hgt'] != height:
                return False
            
            num = height[:-2]
            unit = height[len(num):]

            if unit == 'cm' and (num < '150' or num > '193'):
                return False
            if unit == 'in' and (num < '59' or num > '76'):
                return False
        if key == 'hcl':
            if len(p['hcl']) != 7:
                return False
            m = re.search("#[0-9a-f]{6}", p['hcl'])
            if not m:
                return False
        if key == 'ecl':
            if p['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        if key == 'pid':
            m = re.search("[0-9]{9}", p['pid'])

            if not m:
                return False
            
            sl = slice(m.start(), m.end())
            num = p['pid'][sl]

            if p['pid'] != num:
                return False
    return True

with open(file) as f:
    passports = []
    passenger_information = []
    for i, line in enumerate(f.readlines()):
        info = line.strip().split(" ")
        if line != '\n':
            passenger_information += info
        else:
            p_dict = {item.split(":")[0]:item.split(":")[1] for item in passenger_information}
            passports.append(p_dict)
            passenger_information = []
    else:
        p_dict = {item.split(":")[0]:item.split(":")[1] for item in passenger_information}
        passports.append(p_dict)

print(f"Part 1: {sum(1 for p in passports if is_valid(p))}")
print(f"Part 2: {sum(1 for p in passports if valid_fields(p))}")