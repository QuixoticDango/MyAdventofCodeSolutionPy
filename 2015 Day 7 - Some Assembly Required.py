# import re

# def bitOps(inst):
#     # print(inst['x'])
#     # print(inst['d'])
#     # for key in inst.keys():
#     #     print(key)
#     if not str(inst[key]).isnumeric():    
#         s = re.search(r'AND|OR|NOT|LSHIFT|RSHIFT',inst[key])
#     else:
#         continue
#     direction = inst[key][s.start():s.end()]
#     if direction == "AND":
#         lst = inst[key].split(' AND ')
#         inst[key] = inst[lst[0]] & inst[lst[1]]
#     if direction == "OR":
#         lst = inst[key].split(' OR ')
#         inst[key] = inst[lst[0]] | inst[lst[1]]
#     if direction == "NOT":
#         lst = inst[key].split()
#         inst[key] = ~inst[lst[1]]
#     if direction == "LSHIFT":
#         lst = inst[key].split(' LSHIFT ')
#         inst[key] = inst[lst[0]] << int(lst[1])
#     if direction == "RSHIFT":
#         lst = inst[key].split(' RSHIFT ')
#         inst[key] = inst[lst[0]] >> int(lst[1])
#     # keyVal = []
#     # for key in inst:
#     #     keyVal.append(str(key) + ': ' + str(inst[key]))
#     return keyVal

# filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2015 Day 7 Advent of Code Input.txt"
# with open(filePath, 'r') as f:
#     instructions = {line.strip().split(' -> ')[1]:(int(line.strip().split(' -> ')[0]) 
#                     if line.strip().split(' -> ')[0].isnumeric() 
#                     else line.strip().split(' -> ')[0])
#                     for line in f.readlines()}

# for item in bitOps(instructions):
#     print(item)
# Someone else's solution
filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2015 Day 7 Advent of Code Input.txt"
with open(filePath, 'r') as f:
    commands = [line.strip() for line in f.readlines()]

calc = dict()
results = dict()

for command in commands:
    (ops, res) = command.split('->')
    calc[res.strip()] = ops.strip().split(' ')

def calculate(name):
    try:
        return int(name)
    except ValueError:
        pass

    if name not in results:
        ops = calc[name]
        if len(ops) == 1:
            res = calculate(ops[0])
        else:
            op = ops[-2]
            if op == 'AND':
              res = calculate(ops[0]) & calculate(ops[2])
            elif op == 'OR':
              res = calculate(ops[0]) | calculate(ops[2])
            elif op == 'NOT':
              res = ~calculate(ops[1]) & 0xffff
            elif op == 'RSHIFT':
              res = calculate(ops[0]) >> calculate(ops[2])
            elif op == 'LSHIFT':
              res = calculate(ops[0]) << calculate(ops[2])
        results[name] = res
    return results[name]

print("a: %d" % calculate('a'))