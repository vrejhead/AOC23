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
dictionary = {'|': ((-1, 0), (1, 0)), '-': ((0, -1), (0, 1)), 'L': ((-1, 0), (0, 1)), 'J': ((-1, 0), (0, -1)), '7': ((0, -1), (1, 0)), 'F': ((0, 1), (1, 0)), '.': ()}
visited = set()
def recurse(row, col, direction, layer, homeTile): # logic explained in pt1 code
    global visited
    tile = newText[row][col]
    if (row, col) == homeTile and layer != 0:
        return True
    if (direction[0], direction[1]) not in dictionary[tile]:
        return False
    for dir in dictionary[tile]:
        if dir != direction:
            try:
                assert (row + dir[0]) >= 0
                assert (col + dir[1]) >= 0
                visited.add((row, col))
                return recurse(row + dir[0], col + dir[1], (dir[0] * -1, dir[1] * -1), layer + 1, homeTile)
            except:
                pass
    return False
firstDirection = None
for dir in ((0, 1), (0, -1), (1, 0), (-1, 0)):
    visited.clear()
    if (recurse(s[0] + dir[0], s[1] + dir[1], (-dir[0], -dir[1]), 1, s)):
        if not firstDirection:
            firstDirection = dir
        else:
            for entry, val in dictionary.items(): # this replaces the 'S' with the corrosponding letter so that the inside/outside detection works
                if val == (firstDirection, dir) or val == (dir, firstDirection):
                    newText[s[0]][s[1]] = entry
                    visited.add(s)
            break
inside = 0
specials = {'J': (True), 'L': (True), '7': (False), 'F': (False)} # True is connection to top, False is connecting to bottom
for i, row in enumerate(newText):
    hori = 0
    flag = False
    curSpecialChar = None
    for j, char in enumerate(row):
        if (i, j) in visited: # if its in the path,
            if char == '|': # this always switches the state of inside/outside
                hori += 1
            elif char in specials: # every 2 special chars there is a chance to switch, like F----7 does not switch but F----J does
                if curSpecialChar == None:
                    curSpecialChar = specials[char]
                else:
                    if specials[char] != curSpecialChar: # so uh yeah if the bools are different switch
                        hori += 1
                    curSpecialChar = None
        elif (hori % 2 == 1): # hori could prob be a bool but do not care
            inside += 1
print(inside)
