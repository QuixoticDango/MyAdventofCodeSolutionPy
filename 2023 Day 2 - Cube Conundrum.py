file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 2 Advent of Code Input.txt"

bag = {'r':12, 'g':13, 'b':14}

with open(file) as f:
    lines = [line.strip() for line in f.readlines()]
    games = dict()
    test = False
    for l in lines:
        if test:
            break
        g = ''
        for ch in l:
            if ch.isnumeric():
                g += ch
            if ch == ':':
                key = int(g)
                games[key] = []
                game = l[l.index(':') + 1:].split(';')
                game = [r.strip().split(', ') for r in game]
                for Round in game:
                    round_dict = {'r':0, 'g':0, 'b':0}
                    for marbles in Round:
                        n = int(''.join(ch for ch in marbles if ch.isnumeric()))
                        if 'red' in marbles:
                            round_dict['r'] = n
                        if 'green' in marbles:
                            round_dict['g'] = n
                        if 'blue' in marbles:
                            round_dict['b'] = n
                    games[key].append(round_dict)

# Part 1
s = 0
for key1 in games.keys():
    if all(round[color] <= bag[color] for round in games[key1] for color in round.keys()):
        s += key1
print(s)

# Part 2
s = 0
for game in games.keys():
    min_red = max(round['r'] for round in games[game])
    min_green = max(round['g'] for round in games[game])
    min_blue = max(round['b'] for round in games[game])
    power = min_red * min_green * min_blue
    s += power
print(s)
