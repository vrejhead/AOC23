import sys, re, copy, itertools, functools, math, collections, hashlib, json
with open('input.txt', 'r') as f:
    text = list(map(list, f.read().split('\n')[:-1]))
for r in range(len(text)):
    for c in range(len(text[r])):
        if text[r][c] == 'O':
            if r == 0: # stones dont roll of the topmost row for some reason
                continue
            pointer = r - 1 # start at the row above the stone
            while text[pointer][c] == '.' and pointer >= 0:
                pointer -= 1 # keep going up until the stone cant roll
            text[pointer + 1][c] = 'O' # set the stone
            if pointer + 1 != r: # if the stone didnt move, dont override its position
                text[r][c] = '.'
weight = 0
for r, row in enumerate(text):
    stones = collections.Counter(row)['O']
    weight += stones * (len(text) - r)
print(weight)
