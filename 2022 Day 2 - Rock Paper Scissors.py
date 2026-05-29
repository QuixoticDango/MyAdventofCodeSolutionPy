file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2022 Day 2 Advent of Code Input.txt"

with open(file) as f:
    score = 0
    score_2 = 0
    guide = dict(zip('XYZ', [1, 2, 3]))
    draw = dict(zip('ABC', 'XYZ'))
    opp_options = 'ABC'
    you_options = 'XYZ'

    for line in f.readlines():
        opp, you = line.strip().split()
        if draw[opp] == you:
            score += guide[you] + 3
        elif opp == 'A' and you == 'Y' or opp == 'B' and you == 'Z' or opp == 'C' and you == 'X':
            score += guide[you] + 6
        else:
            score += guide[you] + 0
        if you == 'X':
            score_2 += guide[you_options[(opp_options.index(opp) + 2) % len(opp_options)]] + 0
        if you == 'Y':
            score_2 += guide[you_options[opp_options.index(opp) % len(opp_options)]] + 3
        if you == 'Z':
            score_2 += guide[you_options[(opp_options.index(opp) + 1) % len(opp_options)]] + 6

print(f"Part 1: {score}")
print(f"Part 2: {score_2}")