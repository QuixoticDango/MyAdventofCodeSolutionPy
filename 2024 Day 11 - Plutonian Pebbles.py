def pebbleCount(pList, blinkNum):
    count = 0
    print(pList)
    while count < blinkNum:
        for i in range(len(pList)):
            if pList[i] == 0:
                pList[i] = 1
            elif len(str(pList[i])) % 2 == 0:
                pebble1 = str(pList[i])[:len(str(pList[i])) // 2]
                pebble2 = str(pList[i])[len(str(pList[i])) // 2:]
                print(f"{pebble1}")
                del pList[i]
                p1 = int(pebble1)
                p2 = int(pebble2)
                pList.insert(i, [p1, p2])
            else:
                product = pList[i] * 2024
                pList[i] = product
        count += 1
    print(pList)
    return len(pList)
                

file_path = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2024 Day 11 Advent of Code Input Test.txt"
with open(file_path, 'r') as f:
    pebbles = list(map(int, f.readline().strip().split()))
print(f"{pebbles=}")

print(pebbleCount(pebbles, 2))