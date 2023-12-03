isPart2 = False
numbers = '1234567890'
with open('temp.txt', 'r') as f:
    text = f.read().split('\n')[:-1]
symbolCoords = set()
def checkAdjSymbol(i, j):
    if ((i + 1, j) in symbolCoords) or ((i - 1, j) in symbolCoords) or ((i, j - 1) in symbolCoords) or ((i, j + 1) in symbolCoords) or ((i + 1, j + 1) in symbolCoords) or ((i + 1, j - 1) in symbolCoords) or ((i - 1, j + 1) in symbolCoords) or ((i - 1, j - 1) in symbolCoords):
        return True
    return False
def getAdjNumbers(i, j):
    topSubStr = text[i - 1][j - 3:j + 4]
    bottomSubStr = text[i + 1][j - 3:j + 4]
    print(topSubStr)
for i, row in enumerate(text):
    for j, item in enumerate(row):
        if item not in (numbers + '.'):
            symbolCoords.add((i, j))
total = 0
for i, row in enumerate(text):
    flag = False
    current = ''
    for j, item in enumerate(row):
        if item in (numbers):
            current += item
            if checkAdjSymbol(i, j):
                flag = True
        else:
            if flag:
                flag = False
                total += int(current)
            current = ''
    if flag:
        flag = False
        total += int(current)
print(total)
