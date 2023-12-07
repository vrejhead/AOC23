import copy, json, itertools, collections
with open('input.txt', 'r') as f:
    text = list(map(lambda x: x.split()[1:], f.read().split('\n')[:-1]))
total = 1
for i, (time, dist) in enumerate(zip(text[0], text[1])):
    solves = 0
    for j in range(int(time) + 1):
        vel = j
        if ((int(time) - j) * j) > int(dist):
            solves += 1
    if solves != 0:
        total *= solves
print(total)
