import sys, re, copy, itertools, functools, math, collections, hashlib, json
with open('2023/input.txt', 'r') as f:
    text = f.read()[:-1]
total = 0
def getHash(string):
    tempHash = 0
    for char in string:
        tempHash += ord(char)
        tempHash *= 17
        tempHash %= 256
    return tempHash
boxes = [[None] for _ in range(256)]
focusing = dict()
for x in text.split(','):
    if x[-1] == '-':
        label = x[:-1]
        box = getHash(label)
        try:
            temp = boxes[box].index(label)
            boxes[box].pop(temp)
        except Exception as e:
            pass
    else:
        label = x.split('=')
        box = getHash(label[0])
        focusing[label[0]] = int(label[1])
        try:
            temp = boxes[box].index(label[0])
            boxes[box][temp] = label[0]
        except Exception as e:
            boxes[box].append(label[0])
total = 0
for boxNum, box in enumerate(boxes):
    for slotNum, slot in enumerate(box[1:]):
        total += ((boxNum + 1) * (slotNum + 1) * focusing[slot])
        #print(total, box, slot)
print(total)
