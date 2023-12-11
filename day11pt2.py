import sys, re, copy, itertools, functools, math, collections
with open('input.txt', 'r') as f:
    text = f.read().split('\n')[:-1]
oldText = []
for entry in text:
    oldText.append([(0 if x == '.' else 1) for x in entry])
expandRow = set()
expandCol = set()
for i, row in enumerate(oldText): # which rows should be expanded
    if not any(row):
        expandRow.add(i)
for j in range(len(oldText[0])): # which columns should be expanded
    if not any([oldText[i][j] for i in range(len(oldText))]):
        expandCol.add(j)
galaxies = set()
for i, row in enumerate(oldText):
    for j, char in enumerate(row):
        if char == 1:
            galaxies.add((i, j))
def calcDist(gal1, gal2):
    dist = 0
    expandFactor = 1e6
    for i in range(min(gal1[0], gal2[0]), max(gal1[0], gal2[0]) + 0): # for every row the path takes, if its expanded add the expandFactor instead of 1
        if i in expandRow:
            dist += expandFactor
        else:
            dist += 1
    for i in range(min(gal1[1], gal2[1]), max(gal1[1], gal2[1]) + 0): # same logic for columns
        if i in expandCol:
            dist += expandFactor
        else:
            dist += 1
    return dist
dist = 0
for item in itertools.combinations(galaxies, 2): # yeah this could be faster with sum(map(lambda x: calcDist(x[0], x[1]), (item for item in itertools.combinations(galaxies, 2)))) but do not care
    dist += (calcDist(item[0], item[1]))
print(dist)
