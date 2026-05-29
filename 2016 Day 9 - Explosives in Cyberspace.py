# import re

# filePath = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2016 Day 9 Advent of Code Input.txt"
# with open(filePath) as f:
#     string = f.readline().strip()
#     p1 = re.compile(r'\((\d+x\d+)\)')
#     data = [d for d in re.split(p1, string) if d != '']

# # for _ in data:
# #     if _ in re.findall(p1, data):
# #         print(_)
# # print(f"{string=}")
# while re.search(p1, string) != None:
#     m = re.search(p1, string)
#     numCh, multi = list(map(int, string[m.start()+1:m.end()-1].split('x')))
#     s1 = string[m.end():m.end()+numCh] * multi
#     # print(f"{s1=}")
#     s2 = string[m.end()+numCh:]
#     # print(f"{s2=}")
#     string = s1 + s2
#     # print(f"{string=}")
#     # break

# print(len(string))

from itertools import takewhile, islice

def decompress(data, recurse):
    answer = 0
    chars = iter(data)
    for c in chars:
        if c == '(':
            n, m = map(int, [''.join(takewhile(lambda c: c not in 'x)', chars)) for _ in (0, 1)])
            s = ''.join(islice(chars, n))
            answer += (decompress(s, recurse) if recurse else len(s))*m
        else:
            answer += 1
    return answer

data = open("C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2016 Day 9 Advent of Code Input.txt").read()
print('Answer #1:', decompress(data, False))
print('Answer #2:', decompress(data, True))