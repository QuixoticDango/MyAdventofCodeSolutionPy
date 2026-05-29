filename = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2017 Day 1 Advent of Code Input.txt"
with open(filename) as f:
    captcha = f.read().strip()
k = len(captcha)
key = sum(int(ch) for i,ch in enumerate(captcha) if ch == captcha[(i + 1) % k])
key2 = sum(int(ch) for i,ch in enumerate(captcha) if ch == captcha[(i + k // 2) % k])
print(key)
print(key2)