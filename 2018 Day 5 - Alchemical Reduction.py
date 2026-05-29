file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2018 Day 5 Advent of Code Input.txt"

with open(file, 'rt') as f:
    chain = f.read().strip()

step = ord('a') - ord('A')

def react_units(polymer):
    while any(ch == chr(ord(polymer[i+1]) + step) or ch == chr(ord(polymer[i+1]) - step)
            for i, ch in enumerate(polymer) if i < len(polymer) - 1):
        for i in range(len(polymer)):
            if i < len(polymer) - 1:
                if polymer[i] == chr(ord(polymer[i+1]) + step) or polymer[i] == chr(ord(polymer[i+1]) - step)\
                    and not polymer[i].isspace():
                    if i == len(polymer) - 2:
                        polymer = polymer[:i]
                    else:
                        polymer = polymer[:i] + polymer[i+2:]
    return len(polymer)

def remove_unit(polymer, unit):
    unit = unit.lower()
    new_chain = ''.join(ch for ch in polymer if ch != unit and ch != chr(ord(unit) - step))
    return react_units(new_chain)

units = set(chain.lower())
print(react_units(chain))
print(min(remove_unit(chain, units.pop()) for i in range(len(units))))