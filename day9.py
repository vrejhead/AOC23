import sys, re, copy, itertools, functools, math, collections
with open('input.txt', 'r') as f:
    text = f.read().split('\n')[:-1]
    text = list(map(lambda x: list(map(int, x.split())), text))
flag = False
temp = []
sums = 0
for i in range(len(text)):
    diffs = []
    last = text[i][-1]
    while True:
        temp.clear()
        flag = False
        for j in range(len(text[i]) - 1): # find the difference one layer down
            temp.append(text[i][j + 1] - text[i][j])
            if temp[-1] != 0:
                flag = True
        if temp:
            diffs.append(temp[-1]) # store the last difference since we need to extend
        if flag == False:
            diffs.reverse()
            for k, item in enumerate(diffs[1:]): # just extend the differences it up
                diffs[k + 1] = item + diffs[k]
            sums += (last + diffs[-1])
            break
        else:
            text[i] = temp.copy() # if the list isnt all 0 then remove the layer down into the cur layer
print(sums)
