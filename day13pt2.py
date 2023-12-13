import sys, re, copy, itertools, functools, math, collections
with open('input.txt', 'r') as f:
    text = f.read().split('\n\n')
def checkValidityRow(grid, row):
    smudge = True # there is no error by default
    try:
        for i in range(0, 999):
            assert (row - i - 1) >= 0
            temp = maybe(grid[row - i - 1], grid[row + i], smudge) # if the error is already used up dont allow another one
            if not temp[0]:
                return False, True
            smudge = temp[1]
    except:
        return True, smudge # return if there is a error or not
def checkValidityCol(grid, col):
    smudge = True # there is no error by default
    try:
        for i in range(0, 999):
            assert (col - i - 1) >= 0
            temp = maybe([row[col - i - 1] for row in grid], [row[col + i] for row in grid], smudge) # if the error is already used up dont allow another one
            if not temp[0]:
                return False, True
            smudge = temp[1]
    except:
        return True, smudge # return if there is a error or not
def maybe(line1, line2, flag=True): # flag means to allow an error or not, True=allow, False=dont allow
    for x, y in zip(line1, line2):
        if x != y:
            if flag:
                flag = False
            else:
                return False, None
    return True, flag # return if the error is used or not
total = 0
for grid in text:
    realGrid = grid.split('\n')
    realGrid = (realGrid if realGrid[-1] != '' else realGrid[:-1]) # the last grid has an extra '' at the end
    for i in range(1, len(realGrid)): # i uhh switched it to not use enumerate so i can modify grid during runtime but like didnt need it
        if (temp2 := (checkValidityRow(realGrid, i)))[0]:
            total += (i * 100 if not temp2[1] else 0) # if no errors was used it means that its the original reflection in pt1, so ignore as as we are trying to find new reflection lines
    for col in range(1, len(realGrid[0])):
        if (temp2 := (checkValidityCol(realGrid, col)))[0]:
            total += (col if not temp2[1] else 0) # if no errors was used it means that its the original reflection in pt1, so ignore as as we are trying to find new reflection lines
print(total)
