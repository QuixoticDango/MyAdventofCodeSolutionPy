def updateSum(rules, updates):
    sum = 0
    for update in updates:
        if all(update.index(rule[0]) < update.index(rule[1]) for rule in rules if rule[0] in update and rule[1] in update):
            sum += update[(len(update) - 1) // 2]
    return sum

rules_path = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2024 Day 5 Advent of Code Rules.txt"
updates_path = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2024 Day 5 Advent of Code Updates.txt"

with open(rules_path, 'r') as r:
    rules = [tuple(map(int, s.split('|'))) for s in r.readlines()]

with open(updates_path, 'r') as u:
    updates = [tuple(map(int, t.split(','))) for t in u.readlines()]

print(updateSum(rules, updates))
