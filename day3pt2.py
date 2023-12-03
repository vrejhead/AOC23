isPart2 = False
import os
numbers = '1234567890'
with open('temp.txt', 'r') as f:
    text = f.read().split('\n')[:-1]
symbolCoords = set()
rowLen = len(text[0])
def checkAdjSymbol(i, j):
    if ((i + 1, j) in symbolCoords) or ((i - 1, j) in symbolCoords) or ((i, j - 1) in symbolCoords) or ((i, j + 1) in symbolCoords) or ((i + 1, j + 1) in symbolCoords) or ((i + 1, j - 1) in symbolCoords) or ((i - 1, j + 1) in symbolCoords) or ((i - 1, j - 1) in symbolCoords):
        return True
    return False
def getSomeHelp(i, j):
    outputs = list()
    topSubStr = text[i][max(0, j - 3):min(j + 4, rowLen)]
    topSubStr = ''.join([x if x in numbers else '.' for x in topSubStr])
    print(topSubStr)
    splitTop = [int(x) for x in topSubStr.split('.') if x != '']
    if topSubStr[3] == '.': # middle is "."
        if topSubStr[2] != '.': # so there are actually adj numbers
            if topSubStr[0] == '.': # .##v or ..#v where v has star below and is ".", so the first splits
                outputs.append(splitTop[0])
            elif topSubStr[1] == '.': # #.#v
                outputs.append(splitTop[1])
            else: # ###v
                outputs.append(splitTop[0])
        if topSubStr[4] != '.': # so there are actually adj numbers
            if topSubStr[6] == '.': # v##. or v#..
                outputs.append(splitTop[-1])
            elif topSubStr[5] == '.': # v#.#
                outputs.append(splitTop[-2])
            else: # ###v
                outputs.append(splitTop[-1])
    else: # there can only be one number touching
        if topSubStr[2] != '.': # so there are actually adj numbers
            if topSubStr[0] == '.': # .##v or ..#v
                outputs.append(splitTop[0])
            else: # ###v or # #.#v
                if topSubStr[1] != '.':
                    outputs.append(splitTop[0])
                else:
                    outputs.append(splitTop[1])
        else: # the adj number extends to the right
            if topSubStr[5] == '.': # v#.. or v... or v#.# or v..#
                if topSubStr[6] == '.': # v#.. or v...
                    outputs.append(splitTop[-1])
                else: # v#.# or v..#
                    outputs.append(splitTop[-2])
            else: # v##. or v.#. or v.##
                if topSubStr[4] == '.': # v.## or v.#.
                    outputs.append(splitTop[-2])
                else: # v##.
                    outputs.append(splitTop[-1])
    return outputs
def KYS(i, j):
    outputs = list()
    sideSubStr = text[i][max(0, j - 3):min(j + 4, rowLen)]
    sideSubStr = ''.join([x if x in numbers else '.' for x in sideSubStr])
    print(sideSubStr[:3] + '*' + sideSubStr[4:], 'side')
    splitSide = [int(x) for x in sideSubStr.split('.') if x != '']
    if sideSubStr[2] != '.': # so there are actually adj numbers
        if sideSubStr[0] != '.' and sideSubStr[1] == '.': # #.#*
            outputs.append(splitSide[1])
        else:
            outputs.append(splitSide[0])
    if sideSubStr[4] != '.': # so there are actually adj numbers
        if sideSubStr[6] != '.' and sideSubStr[5] == '.': # *#.#
            outputs.append(splitSide[-2])
        else:
            outputs.append(splitSide[-1])
    return outputs
def getAdjNumbers(i, j):
    outputs = list()
    if i > 0:
        if (temp := getSomeHelp(i - 1, j)) != []:
            outputs += temp
    if (temp := KYS(i, j)) != []:
        outputs += temp
    if i < len(text):
        if (temp := getSomeHelp(i + 1, j)) != []:
            outputs += temp
    if len(outputs) == 2:
        return outputs[0] * outputs[1]
    return 0
for i, row in enumerate(text):
    for j, item in enumerate(row):
        if item in '*':
            symbolCoords.add((i, j))
total = 0
for coords in symbolCoords:
    temp = getAdjNumbers(*coords)
    print(temp)
    total += temp
    # os.system('pause')
print(total)
