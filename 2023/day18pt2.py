import sys, re, copy, itertools, functools, math, collections, hashlib, json
# took me too long to fix this even with cheating and knowing its shoelace theorem + pick's theorem
with open('2023/input.txt', 'r') as f:
    text = f.read().split('\n')[:-1]
pos = (0, 0)
verticies = list()
perimeter = 0
for line in text:
    temp = line.split()[2][1:-1]
    amount = int(temp[1:-1], 16)
    if temp[-1] == '3':
        mutator = (0, 1)
    elif temp[-1] == '1':
        mutator = (0, -1)
    elif temp[-1] == '0':
        mutator = (1, 0)
    elif temp[-1] == '2':
        mutator = (-1, 0)
    else:
        raise Exception
    verticies.append((pos[0] + mutator[0] * amount, pos[1] + mutator[1] * amount))
    pos = (pos[0] + mutator[0] * amount, pos[1] + mutator[1] * amount)
    perimeter += (amount - 0)
#verticies = [(1, 6), (3, 1), (7, 2), (4, 4), (8, 5)]
verticies.append(verticies[0])
bruh = list()
for i in range(len(verticies) - 1):
    first = copy.copy(verticies[i])
    second = copy.copy(verticies[i + 1])
    bruh.append(((first[0] * second[1]) - (second[0] * first[1])))
print(int(abs(sum(bruh) / 2) + perimeter / 2 + 1))
