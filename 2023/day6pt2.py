import copy, json, itertools, collections
with open('input.txt', 'r') as f:
    text = list(map(lambda x: x.replace(' ', '').split(':')[1:], f.read().split('\n')[:-1]))
    text = [int(text[0][0]), int(text[1][0])]
print(text)
for i in range(text[0] + 1):
    if ((text[0] - i) * i) > text[1]:
        lowerBound = i
        break
for i in range( text[0], 0, -1):
    if ((text[0] - i) * i) > text[1]:
        print(i - lowerBound + 1)
        break
