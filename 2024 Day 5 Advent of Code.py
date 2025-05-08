# This function sums the central number of the correct updates.
def updateSum(rules, updates):
    sum = 0
    for update in updates:
        if all(update.index(rule[0]) < update.index(rule[1]) for rule in rules if rule[0] in update and rule[1] in update):
            sum += update[(len(update) - 1) // 2]
    return sum
# This function is corrects the incorrect updates and sums the central number.
def fixedUpdateSum(rules, updates):

    # Build list of good updates.
    # If update is in good list, continue to the next update without doing anything.
    # Setting check to False should only be done when it's time to move to the next update.
    # The update is done when it fulfills the right condition
    sum = 0
    good_updates = [update for update in updates if all(update.index(rule[0]) < update.index(rule[1]) for rule in rules if rule[0] in update and rule[1] in update)]
    for update in updates:
        if update in good_updates:
            continue
        else:
            check = False
            while not check:
                for rule in rules:
                    if rule[0] in update and rule[1] in update:
                        if update.index(rule[0]) > update.index(rule[1]):
                            i = update.index(rule[0])
                            j = update.index(rule[1])
                            update[i], update[j] = update[j], update[i]
                            check = all(update.index(r[0]) < update.index(r[1]) for r in rules if r[0] in update and r[1] in update)
        sum += update[(len(update) - 1) // 2]
    return sum

rules_path = "C:\\Users\\ANON\\Documents\\Coding and Programming Folder\\2024 Day 5 Advent of Code Rules.txt"
updates_path = "C:\\Users\\ANON\\Documents\\Coding and Programming Folder\\2024 Day 5 Advent of Code Updates.txt"

with open(rules_path, 'r') as r:
    rules = [list(map(int, s.split('|'))) for s in r.readlines()]

with open(updates_path, 'r') as u:
    updates = [list(map(int, t.split(','))) for t in u.readlines()]

print(updateSum(rules, updates))
print(fixedUpdateSum(rules, updates))
