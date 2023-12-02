isPart2 = False
with open(r'input.txt', 'r') as f:
    text = f.read().split('\n')
    text = list(map(lambda x: x.split(': ')[1], text[:-1]))
    text = list(map(lambda x: x.split('; '), text))
maximum = {'red': 12, 'green': 13, 'blue': 14}
invalid = 0
power = 0
for i, game in enumerate(text):
    flag = False
    minimum = {'red': 0, 'green': 0, 'blue': 0}
    for result in game:
        temp = result.split(', ')
        for dice in temp:
            temp2 = dice.split()
            if isPart2:
                if minimum[temp2[1]] < int(temp2[0]):
                    minimum[temp2[1]] = int(temp2[0])
            else:
                if maximum[temp2[1]] < int(temp2[0]):
                    invalid += (i + 1)
                    flag = True
                    break
        if flag:
            break
    if isPart2:
        temp3 = 1
        for value in minimum.values():
            temp3 *= value
        power += temp3
if isPart2:
    print(power)
    raise SystemExit
total = ((i + 1) * (i + 2)) * 0.5
print(total - invalid)
