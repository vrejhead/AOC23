with open('input.txt', 'r') as f:
    text = f.read().split('\n')[:-1]
    text = list(map(lambda x: x.split(': ')[1:], text))
total = 0
for i, item in enumerate(text):
    winners = 0
    temp = item[0].split(' | ')
    winning = list(map(int, temp[0].split()))
    have = list(map(int, temp[1].split()))
    for num in winning:
        if num in have:
            winners += 1
    if winners != 0:
        total += (2 ** (winners - 1))
print(total)
