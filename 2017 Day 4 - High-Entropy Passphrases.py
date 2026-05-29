filename = "C:\\Users\\lyndo\\Documents\\Coding and Programming Folder\\2017 Day 4 Advent of Code Input.txt"

with open(filename) as f:
    passphrases = [line.strip().split() for line in f.readlines()]

validPhrasesCount = sum(1 for phrase in passphrases if not any(w == phrase[j] for i,w in enumerate(phrase) for j in range(len(phrase)) if i != j))
validPhrases = [phrase for phrase in passphrases if not any(w == phrase[j] for i,w in enumerate(phrase) for j in range(len(phrase)) if i != j)]
print(validPhrasesCount)

newValidPhrases = 0
valid = 0
check = False

for phrase in passphrases:
    phraseSet = set(''.join(sorted(word)) for word in phrase)
    print(phraseSet)
    if len(phraseSet) == len(phrase):
        valid += 1

print(valid)