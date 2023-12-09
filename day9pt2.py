import sys, re, copy, itertools, functools, math, collections
with open('input.txt', 'r') as f:
    text = f.read().split('\n')[:-1]
    text = list(map(lambda x: list(map(int, x.split())), text))
flag = False
temp = []
sums = 0
for i in range(len(text)):
    diffs = []
    first = text[i][0]
    while True:
        temp.clear()
        flag = False
        for j in range(len(text[i]) - 1): # find the difference one layer down
            temp.append(text[i][j + 1] - text[i][j])
            if temp[-1] != 0:
                flag = True
        if temp:
            diffs.append(temp[0]) # store the first difference since we need to extend backwards
        if flag == False:
            diffs.reverse()
            for k, item in enumerate(diffs[1:]): # just extend the differences up
                diffs[k + 1] = item - diffs[k]
            sums += (first - diffs[-1])
            break
        else:
            text[i] = temp.copy() # if the list isnt all 0 then remove the layer down into the cur layer
print(sums)
