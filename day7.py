import sys, re, copy, itertools, functools, math, collections
with open('input.txt', 'r') as f:
    text = f.read().split('\n')[:-1]
order = '23456789TJQKA'
text = list(map(lambda x: x.split(), text))
def rankStrength(hand):
    hand = list(hand)
    hand.sort(key=lambda x: order.find(x))
    stats = collections.Counter(hand)
    if len(set(hand)) == 1:
        return 5
    if len(set(hand)) == 2:
        if stats.most_common()[0][1] == 4:
            return 4
        if stats.most_common()[0][1] == 3 and stats.most_common()[1][1] == 2:
            return 3
    if len(set(hand)) == 3:
        if stats.most_common()[0][1] == 2 and stats.most_common()[1][1] == 2:
            return 1
        elif stats.most_common()[0][1] == 3 and (stats.most_common()[1][1] == 1) and stats.most_common()[2][1] == 1:
            return 2
    if len(set(hand)) == 4:
        if stats.most_common()[0][1] == 2 and (stats.most_common()[1][1] == stats.most_common()[2][1] == stats.most_common()[3][1] == 1):
            return 0
    if (len(set(hand))) == 5:
        return -1
def dataRank(bruh):
    hand = list(map(lambda x: order.find(x), bruh))
    (temp := (10000000000 * hand[0] + 100000000 * hand[1] + 1000000 * hand[2] + 10000 * hand[3] + 100 * hand[4] + (10 ** 100) * (rankStrength(bruh) + 2)))
    return temp
text.sort(key = lambda x: dataRank(x[0]))
winner = 0
for i, item in enumerate(text):
    winner += (int(item[1]) * (i + 1))
print(winner)
