import sys, re, copy, itertools, functools, math, collections
with open('temp.txt', 'r') as f:
    text = f.read().split('\n')[:-1]
def isValid(springs, stats):
    bands = tuple(len(y) for y in (x for x in ''.join(springs).split('.') if x))
    #print(stats, bands)
    return bands == stats
total = 0
for j, line in enumerate(text):
    if j != 1 and False:
        continue
    stats = tuple(map(int, line.split()[1].split(',')))
    springs = list(line.split()[0])
    damaged = collections.Counter(springs)['?']
    for i in range(1 << damaged):
        occurences = 0
        tempSprings = list()
        for char in springs:
            if char == '?':
                if ((1 << occurences) & i):
                    tempSprings.append('#')
                else:
                    tempSprings.append('.')
                occurences += 1
            else:
                tempSprings.append(char)
        #print(tempSprings)
        total += bool(isValid(tempSprings, stats))
    if j % 10 == 0:
        print(j)
print(total)
