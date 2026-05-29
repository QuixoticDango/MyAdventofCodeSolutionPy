file = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2025 Day 1 Advent of Code Input.txt"

with open(file, 'rt') as f:
    commands = [line.strip() for line in f.readlines()]
    commands = [int(line[1:]) if line[0] == 'R' else -int(line[1:]) for line in commands]
    start = 50
    current = start
    s = 0
    dial = [i for i in range(100)]
    # for command in commands:
        # if 50 + command < 0:
        #     dial = (dial + command + 100) % 100
        # else:
        #     dial = (dial + command) % 100
        # if dial == 0:
        #     s += 1
    for number in commands:
        count = 0
        if number < 0:
            while count > number:
                current -= 1
                # print("RIGHT")
                # print(f"{current=}")
                # print(f"{dial[current % len(dial)]=}")
                if dial[current % len(dial)] == 0:
                    s += 1
                count -= 1
        else:
            while count < number:
                current += 1
                # print('LEFT')
                # print(f"{current=}")
                # print(f"{dial[current % len(dial)]=}")
                if dial[current % len(dial)] == 0:
                    s += 1
                count += 1
print(s)