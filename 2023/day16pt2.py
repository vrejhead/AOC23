import sys, re, copy, itertools, functools, math, collections, hashlib, json
with open('2023/input.txt', 'r') as f:
    text = f.read().split('\n')[:-1]
    text = [list(row) for row in text]
start = [[0, 0], [0, 1]]
rowCount = len(text)
colCount = len(text[0])
visited = set()
unique = set()
sys.setrecursionlimit(10 ** 5)
def light(pos, dir):
    pos = [pos[0] + dir[0], pos[1] + dir[1]]
    if pos[0] < 0 or pos[1] < 0:
        return None
    elif pos[0] >= rowCount or pos[1] >= colCount:
        return None
    if (tuple(pos), tuple(dir)) in visited:
        return None
    #print(f'visiting {pos}')
    tile = text[pos[0]][pos[1]]
    visited.add((tuple(pos), tuple(dir)))
    unique.add(tuple(pos))
    if tile == '.':
        return light(pos, dir)
    elif tile == '|':
        if dir[0] != 0:
            return light(pos, dir)
        else:
            return light(pos, [1, 0]), light(pos, [-1, 0])
    elif tile == '-':
        if dir[1] != 0:
            return light(pos, dir)
        else:
            return light(pos, [0, 1]), light(pos, [0, -1])
    elif tile == '/':
        if dir[0] != 0:
            return light(pos, [0, -dir[0]])
        else:
            return light(pos, [-dir[1], 0])
    elif tile == '\\':
        if dir[1] != 0:
            return light(pos, [dir[1], 0])
        else:
            return light(pos, [0, dir[0]])
scores = set()
for i in range(colCount):
    print(i, ' rows')
    light([-1, i], [1, 0])
    scores.add(len(unique))
    visited.clear()
    unique.clear()
    light([rowCount, i], [-1, 0])
    scores.add(len(unique))
    visited.clear()
    unique.clear()
for i in range(rowCount):
    print(i, ' cols')
    light([i, -1], [0, 1])
    scores.add(len(unique))
    visited.clear()
    unique.clear()
    light([i, colCount], [0, -1])
    scores.add(len(unique))
    visited.clear()
    unique.clear()
#print(visited)
print(max(scores))
