import sys, re, copy, itertools, functools, math, collections
with open('input.txt', 'r') as f:
    text = f.read().split('\n\n')
instructions = text[0]
leMap = dict()
places = list()
for mapping in text[1].split('\n')[:-1]:
    temp = mapping.split(' = ')
    dest = temp[1].split(', ')
    leMap[temp[0]] = (dest[0][1:], dest[1][:-1])
    if temp[0][2] == 'A':
        places.append(temp[0])
LCMs = [0] * len(places)
for j, instruction in enumerate(itertools.cycle(instructions)):
    for i, place in enumerate(places):
        if instruction == 'R':
            places[i] = leMap[place][1]
        else:
            places[i] = leMap[place][0]
    for k, place in enumerate(places):
        if place[2] == 'Z':
            LCMs[k] = (j + 1)
    if all(LCMs):
        print(math.lcm(*LCMs))
        exit(0)
