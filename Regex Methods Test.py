import re

string = input().split("do()")
print(string)

print([re.search(r"don't\(\)", strng) for strng in string])