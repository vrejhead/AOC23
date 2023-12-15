import sys, re, copy, itertools, functools, math, collections
with open('input.txt', 'r') as f:
    text = f.read().split('\n\n')
instructions = text[0]
leMap = dict()
for mapping in text[1].split('\n')[:-1]:
    temp = mapping.split(' = ')
    dest = temp[1].split(', ')
    leMap[temp[0]] = (dest[0][1:], dest[1][:-1])
place = 'AAA'
for steps, instruction in enumerate(itertools.cycle(instructions)):
    if instruction == 'R':
        place = leMap[place][1]
    else:
        place = leMap[place][0]
    steps += 1
    if place == 'ZZZ':
        print(steps)
        exit(0)
