# btw using pt2 code with expandFactor set to 1 also works, but this was my first attempt, and if i had used my pt2 logic to start i prob coulve finished pt1 faster so L
import sys, re, copy, itertools, functools, math, collections
with open('input.txt', 'r') as f:
    text = f.read().split('\n')[:-1]
oldText = []
for entry in text:
    oldText.append([(0 if x == '.' else 1) for x in entry])
expand = set()
newText = []
for i, row in enumerate(oldText):
    newText.append(row)
    if not any(row):
        newText.append(row) # add an extra row if the row is all empty
newerText = [[0] for i in range(len(newText))]
for j in range(len(newText[0])):
    for i in range(len(newText)):
        if j == 0:
            newerText[i][j] = newText[i][j]
        else:
            newerText[i].append(newText[i][j])
    if not any([newText[i][j] for i in range(len(newText))]): # add an extra col if the col is all empty, except scuffed cause no empty arrays :(
        for i in range(len(newText)):
            if j == 0:
                newerText[i][j] = 0
            else:
                newerText[i].append(0)
galaxies = set()
for i, row in enumerate(newerText):
    for j, char in enumerate(row):
        if char == 1:
            galaxies.add((i, j))
dist = 0
for item in itertools.combinations(galaxies, 2):
    dist += (abs(item[0][0] - item[1][0]) + abs(item[0][1] - item[1][1]))
print(dist)
