import sys, re, copy, itertools, functools, math, collections, hashlib, json
# honestly just change the pt2 code this is scuffed, basically it outlines the perimeter, then floodfills from a set position(yeah i told you its bad)
with open('2023/input,txt', 'r') as f:
    text = f.read().split('\n')[:-1]
pos = (0, 0)
visited = set()
visited.add((0, 0))
for line in text:
    temp = line.split()
    if temp[0] == 'U':
        mutator = (0, 1)
    elif temp[0] == 'D':
        mutator = (0, -1)
    elif temp[0] == 'R':
        mutator = (1, 0)
    elif temp[0] == 'L':
        mutator = (-1, 0)
    else:
        raise Exception
    for i in range(int(temp[1])):
        visited.add((pos[0] + mutator[0], pos[1] + mutator[1]))
        pos = (pos[0] + mutator[0], pos[1] + mutator[1])
xExtrema = (min(visited, key=lambda x: x[0])[0], max(visited, key=lambda x: x[0])[0])
yExtrema = (min(visited, key=lambda x: x[1])[1], max(visited, key=lambda x: x[1])[1])
xDiff, yDiff = (xExtrema[1] - xExtrema[0] + 1, yExtrema[1] - yExtrema[0] + 1)
print(xExtrema, xDiff, yExtrema, yDiff)
matrix = [['.' for i in range(xDiff)] for j in range(yDiff)]
for visit in visited:
    matrix[visit[1] - yExtrema[0]][visit[0] - xExtrema[0]] = '#'
matrix = list(reversed(matrix))
floodQueue = collections.deque()
floodQueue.append((10, 100))
done = 0
try:
    #raise Exception
    while True:
        row, col = floodQueue.popleft()
        if matrix[row][col] == '#':
            continue
        done += 1
        matrix[row][col] = '#'
        if row > 0 and matrix[row - 1][col] == '.':
            floodQueue.append((row - 1, col))
        if row < (yDiff - 1) and matrix[row + 1][col] == '.':
            floodQueue.append((row + 1, col))
        if col > 0 and matrix[row][col - 1] == '.':
            floodQueue.append((row, col - 1))
        if col < (xDiff - 1) and matrix[row][col + 1] == '.':
            floodQueue.append((row, col + 1))
except Exception as e:
    with open('output.txt', 'w') as f:
        for line in matrix:
            f.write(''.join(line) + '\n')
    total = 0
    for line in matrix:
        total += collections.Counter(line)['#']
    print(total)
