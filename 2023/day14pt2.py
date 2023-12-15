import sys, re, copy, itertools, functools, math, collections, hashlib, json
with open('input.txt', 'r') as f:
    text = list(map(list, f.read().split('\n')[:-1]))
# actual logic explaination for this is in pt1
def tiltNorth(isSouth=False): # instead of doing logic for south just reverse the order of the rows
    global text
    if isSouth:
        text.reverse()
    for r in range(len(text)):
        for c in range(len(text[r])):
            if text[r][c] == 'O':
                if r == 0:
                    continue
                pointer = r - 1
                while text[pointer][c] == '.' and pointer >= 0:
                    pointer -= 1
                text[pointer + 1][c] = 'O'
                if pointer + 1 != r:
                    text[r][c] = '.'
    if isSouth:
        text.reverse()
def tiltWest(isEast=False): # same but reverse the rows
    global text
    for r in range(len(text)):
        tempRow = copy.copy(text[r])
        if isEast:
            tempRow.reverse()
        for c in range(len(tempRow)):
            if tempRow[c] == 'O':
                if c == 0:
                    continue
                pointer = c - 1
                while tempRow[pointer] == '.' and pointer >= 0:
                    pointer -= 1
                tempRow[pointer + 1] = 'O'
                if pointer + 1 != c:
                    tempRow[c] = '.'
        text[r] = copy.copy(tempRow) if not isEast else list(reversed(tempRow))
def cycle():
    tiltNorth()
    tiltWest()
    tiltNorth(True)
    tiltWest(True)
def getHash():
    return hashlib.sha256(bytes(json.dumps(text), encoding='utf-8')).hexdigest()
cache = dict()
spins = int(1e9)
for i in range(spins):
    preHash = getHash()
    if preHash in cache: # if we already visited this position before then its in a loop
        cyclesLeft = (spins - i) % (i - cache[preHash]) # number of cycles still need to do
        for _ in range(cyclesLeft):
            cycle()
        break
    else:
        cycle()
        cache[preHash] = i
weight = 0
for r, row in enumerate(text):
    stones = collections.Counter(row)['O']
    weight += stones * (len(text) - r)
print(weight)
