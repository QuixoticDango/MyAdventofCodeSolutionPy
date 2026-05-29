import re, sys

filename = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2017 Day 7 Advent of Code Input.txt"

with open(filename) as f:
    lines = [line.strip().split() for line in f.readlines()]
    pattern = re.compile(r'[0-9]+')
    for l in lines:
        match = re.search(pattern, l[1])
        start = match.start()
        end = match.end()
        num = int(l[1][start:end])
        l[1] = num
        if '->' in l:
            del l[2]
        
    towerDict = {l[0]:l[1:] for l in lines}
    for key in towerDict.keys():
        for i,item in enumerate(towerDict[key]):
            if i != 0:
                if item[-1] == ',':
                    item = item[:-1]
                    del towerDict[key][i]
                    towerDict[key].insert(i, item)

bottom = [key for key in towerDict.keys() if all(key not in towerDict[k] for k in towerDict.keys())][0]
print(bottom)

def balanceWeight(d):
    weights = [0 for i in range(len(towerDict[bottom]) - 1)]
    towers = [k for i,k in enumerate(towerDict[bottom]) if i !=0]
    lowestTowers = list(map(list,zip(towers, weights)))
    print(lowestTowers)

    # for key in lowestTowers:
    #     for i,weight in enumerate(weights):
    #         weights[i] += weight
            
    # floor = towerDict[bottom]
    # if all(len(towerDict[tower]) == 1 for tower in floor):
    #     return
    
    # for key in floor:
        
# while True:
#     weights = [0 for i in range(len(towerDict[bottom]) - 1)]
#     towers = [k for i,k in enumerate(towerDict[bottom]) if i !=0]
#     lowestTowers = list(map(list,zip(towers, weights)))
#     for i, l in enumerate(lowestTowers):
#         lowestTowers[i][1] += towerDict[lowestTowers[i][0]][0]
#     print(lowestTowers)
#     break

# balanceWeight(towerDict)

ans = 0
children = dict()
values = dict()
all_kids = set()
total = set()
for line in open(filename).readlines():
    a = list(line.replace(',','').strip().split())
    val = a[0]
    print(f"{val=}")
    values[val] = int(a[1].replace('(','').replace(')',''))
    print(f"{values=}")
    kids = a[3:]
    print(f"{kids=}")
    children[val] = kids
    print(f"{children=}" )
    total.add(val)
    for kid in kids:
        all_kids.add(kid)
ans = (total - all_kids).pop()
print(ans)

def calc_kids_weights(root):
    kid_weights = []
    for kid in children[root]:
        kid_weights.append(calc_weight(kid))
    return kid_weights


def check_bal(root):
    if children[root] == []:
        return True
    kid_weights = calc_kids_weights(root)
    return len(set(kid_weights)) == 1

def unbalanced_kid(root):
    kid_weights = calc_kids_weights(root)
    for kid in children[root]:
        curr_weight = calc_weight(kid)
        if kid_weights.count(curr_weight) == 1:
            return kid

def calc_weight(root):
    tot = values[root]
    for kid in children[root]:
        tot += calc_weight(kid)
    return tot

ans_parent = ans
while not check_bal(ans):
    ans_parent = ans
    ans = unbalanced_kid(ans)
another_kid = children[ans_parent][0]
if another_kid == ans:
    another_kid = children[ans_parent][1]
print(values[ans] - calc_weight(ans) + calc_weight(another_kid))