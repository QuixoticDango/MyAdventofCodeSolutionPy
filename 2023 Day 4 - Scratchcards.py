def product(n):
    p = 1
    for t in n:
        p *= t
    return p

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 4 Advent of Code Input.txt"

with open(file, 'rt') as f:
    cards = [line.strip() for line in f.readlines()]

# Part 1 with some preparations for Part 2
score = 0
multipliers = dict()
for i, card in enumerate(cards, 1):
    colon = card.index(':')
    card_key = card[:colon]
    card_key = "Card " + ''.join(ch for ch in card_key if ch.isnumeric()) 
    multipliers[card_key] = [1, 0]
    winning_nums, actual_nums = card[colon + 1:].strip().split(' | ')
    winning_nums = set(winning_nums.split())
    actual_nums = set(actual_nums.split())
    winners = winning_nums.intersection(actual_nums)
    if len(winners) > 0:
        score += 2**(len(winners) - 1)
print(score)

# Part 2

for i, card in enumerate(cards, 1):
    winning_nums, actual_nums = card[colon + 1:].strip().split(' | ')
    winning_nums = set(winning_nums.split())
    actual_nums = set(actual_nums.split())
    winners = winning_nums.intersection(actual_nums)
    multipliers["Card " + str(i)][1] += len(winners)
    instances = multipliers["Card " + str(i)][0]
    for inst in range(1, instances + 1):
        counter = 1
        while counter <= len(winners):
            multipliers[f"Card " + str(i + counter)][0] += 1
            counter += 1
print(multipliers)
print(sum(multipliers[key][0] for key in multipliers.keys()))