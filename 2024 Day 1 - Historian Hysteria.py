def lstdst(lst1, lst2):
    lst1.sort()
    lst2.sort()

    sum = 0
    for i in range(len(lst1)):
        diff = abs(lst1[i] - lst2[i])
        sum += diff
    return sum

def lstsim(lst1, lst2):
    lst1.sort()
    lst2.sort()

    # 3   4   sorted:   1   3
    # 4   3             2   3
    # 2   5             3   3
    # 1   3             3   4
    # 3   9             3   5
    # 3   3             4   9
    counter_d = dict()
    sim_score = 0
    if lst1[0] > lst2[-1] or lst1[-1] < lst2[0]:
        return 0
    
    for i in range(len(lst1)):
        counter = 0
        for j in range(len(lst2)):
            if lst1[i] in counter_d.keys():
                sim_score += counter_d[lst1[i]] * lst1[i]
                break
            if lst1[i] == lst2[j]:
                counter += 1
            if lst1[i] < lst2[j]:
                counter_d[lst1[i]] = counter
                sim_score += counter * lst1[i]
                break
    return sim_score
            


rows = [0]
lst1 = []
lst2 = []
while True:
    rows = input().split()
    if not rows:
        break
    lst1.append(int(rows[0]))
    lst2.append(int(rows[1]))

print("The list distance is", lstdst(lst1, lst2))
print("The list similarity is", lstsim(lst2, lst1))
