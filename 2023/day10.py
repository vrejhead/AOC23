import sys, re, copy, itertools, functools, math, collections
with open('input.txt', 'r') as f:
    text = f.read().split('\n')[:-1]
newText = []
for entry in text:
    newText.append(list(entry))
for i, row in enumerate(newText):
    for j, col in enumerate(row):
        if col == 'S':
            s = (i, j)
sys.setrecursionlimit(10000000)
dictionary = {'|': ((-1, 0), (1, 0)), '-': ((0, -1), (0, 1)), 'L': ((-1, 0), (0, 1)), 'J': ((-1, 0), (0, -1)), '7': ((0, -1), (1, 0)), 'F': ((0, 1), (1, 0)), '.': ()} # where the tiles connect to
def recurse(row, col, direction, layer, homeTile):
    tile = newText[row][col]
    if (row, col) == homeTile and layer != 0:
        return layer # if the loop is complete return layer(aka length of the loop)
    if (direction[0], direction[1]) not in dictionary[tile]:
        return 0 # if this tile does not connect in the direction
    for dir in dictionary[tile]: # where this tile can be connected
        if dir != direction: # if its not from where we came from
            try:
                assert (row + dir[0]) >= 0 # some assert statements because negative indexing
                assert (col + dir[1]) >= 0
                return recurse(row + dir[0], col + dir[1], (dir[0] * -1, dir[1] * -1), layer + 1, homeTile) # dir is negated because its from the perspective of the cur tile not the future tile
            except:
                pass
    return 0
total = 0
for dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
    total = max(total, recurse(s[0] + dir[0], s[1] + dir[1], (-dir[0], -dir[1]), 1, s)) # this could prob be simpler but dont care
print(total // 2)
