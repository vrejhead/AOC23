import sys, re, copy, itertools, functools, math, collections, hashlib, json
with open('2023/input.txt', 'r') as f:
    text = f.read()[:-1]
total = 0
for x in text.split(','):
    print(x)
    tempHash = 0
    for char in x:
        tempHash += ord(char)
        tempHash *= 17
        tempHash %= 256
    total += tempHash
    print(tempHash)
print(total)
