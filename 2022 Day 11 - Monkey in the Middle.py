from copy import deepcopy

class monkey:
    monkey_count = 0

    def __init__(self, starting_items: list[int], operation: list[str],
                 test: int, outcomes: tuple[int, int]):
        monkey.monkey_count += 1
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.outcomes = outcomes
        self.lcm = 2 * 19 * 13 * 17 * 5 * 3 * 7 * 11

    def execute_operation(self) -> None:
        new_worry_vals: list[int] = []
        for w in self.items:
            local_vars = {}
            exec(' '.join(self.operation).replace('old', str(w)), globals(), local_vars)
            new_worry_vals.append(local_vars['new'])
        self.items = [v % self.lcm for v in new_worry_vals]
        # print(f"{self.items = }")
    
    def apply_test(self) -> list[int]:
        idx_lst: list[int] = []
        for w in self.items:
            if w % self.test == 0:
                idx_lst.append(self.outcomes[0])
            else:
                idx_lst.append(self.outcomes[1])
        # print(f"{idx_lst = }")
        return idx_lst
    
    def toss(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def catch(self, item):
        self.items.append(item)
    
    def __str__(self):
        return "items: " + ', '.join(map(str,self.items)) + '\n' + "operation: " + ' '.join(self.operation)\
        + "\ntest: " + str(self.test) + "\noutcomes: " + "monkey " + str(self.outcomes[0]) + " if true"\
        + ", otherwise monkey " + str(self.outcomes[1])

file: str = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2022 Day 11 Advent of Code Input.txt"

with open(file) as f:
    monke_lst: list[monkey] = []
    for line in f.readlines():
        l = line.strip()
        if "Monkey" in l:
            continue
        if "items" in l:
            starting_items = list(map(int, l[16:].split(', ')))
        if "Operation" in l:
            operation = l[11:].split()
            # exec(' '.join(operation).replace('old', str(25)))
            # print("DID IT")
            # print(f"{new = }")
            # print()
        if "Test" in l:
            test = int(''.join(ch for ch in line if ch.isnumeric()))
        if 'true' in l:
            outcomes = int(l[-1]),
        if 'false' in l:
            outcomes += int(l[-1]),
        if not l:
            # print(f"{outcomes = }")
            monke_lst.append(monkey(starting_items, operation, test, outcomes))
            outcomes = None
    else:
        monke_lst.append(monkey(starting_items, operation, test, outcomes))

orig_monke_lst = deepcopy(monke_lst)
inspection_count = {i:0 for i in range(len(monke_lst))}
round = 0
while round < 20:
    for i, m in enumerate(monke_lst):
        m.execute_operation()
        inspection_count[i] += len(m.items)
        idxs = m.apply_test()
        for idx in idxs:
            monke_lst[idx].catch(m.toss())
    round += 1

count = [v for k,v in inspection_count.items()]
count.sort(reverse=True)
print(f"Part 1: {count[0] * count[1]}")

inspection_count = {i:0 for i in range(len(monke_lst))}
round = 0
while round < 10000:
    for i, m in enumerate(orig_monke_lst):
        m.execute_operation()
        inspection_count[i] += len(m.items)
        idxs = m.apply_test()
        for idx in idxs:
            orig_monke_lst[idx].catch(m.toss())
    round += 1
count = [v for k,v in inspection_count.items()]
count.sort(reverse=True)
print(f"Part 2: {count[0] * count[1]}")