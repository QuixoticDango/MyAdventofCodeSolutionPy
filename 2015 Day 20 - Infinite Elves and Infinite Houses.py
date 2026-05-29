def countPresents(houseNum):
    factors = set()
    factors.add(1)
    factors.add(houseNum)
    for n in range(2, int(houseNum**0.5) + 1):
        if houseNum % n == 0:
            factors.add(n)
            factors.add(houseNum // n)
    numPresents = 0
    while len(factors) > 0:
        numPresents += factors.pop()
    return numPresents

def countPresents2(houseNum):
    numPresents = 0
    if houseNum < 50:
        print('Reached part 1')
        return countPresents(houseNum)
    
    numPresents = houseNum*11 + sum(11 * n for n in range(houseNum // 50, houseNum // 2 + 1) if houseNum % n == 0)

    # factors = set()
    # factors.add(houseNum)
    
    # for n in range(houseNum // 50, houseNum // 2 + 1):
    #     if houseNum % n == 0:
    #         factors.add(n)

    # numPresents = sum(factors)
    return numPresents

i = 705000
while countPresents2(i) < 29000000:
    # print(f"{i=}")
    # print(f"{countPresents2(i)}")
    i += 1
print(f"{i}")

# import numpy as np

# goal = 29000000
# BIG_NUM = 1000000
# houses = np.zeros(BIG_NUM)
# for elf in range(1, BIG_NUM):
#     houses[elf:(elf+1)*50:elf] += 11 * elf
# print(np.nonzero(houses >= goal)[0][0])