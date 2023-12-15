with open('input.txt', 'r') as f:
    text = f.read().split('\n')[:-1]
    text = list(map(lambda x: x.split(': ')[1:], text))
from collections import defaultdict
total = 0
result = defaultdict(int)
print(result)
for i, item in enumerate(text):
    winners = 0
    temp = item[0].split(' | ')
    winning = list(map(int, temp[0].split()))
    have = list(map(int, temp[1].split()))
    for num in winning:
        if num in have:
            winners += 1
    result[i] = winners
cards = defaultdict(int)
for i in range(len(text)):
    cards[i] = 1
for key, value in result.items():
    for i in range(cards[key]):
        for i in range(value):
            cards[i + key + 1] += 1
print(sum(cards.values()))
