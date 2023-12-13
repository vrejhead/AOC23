import sys, re, copy, itertools, functools, math, collections
with open('input.txt', 'r') as f:
    text = f.read().split('\n\n')
def checkValidityRow(grid, row): # given the row of reflection validates all other visible rows are indeed reflections
    try:
        for i in range(0, 999):
            assert (row - i - 1) >= 0 # negative indexing is a blessing and a curse
            if grid[row - i - 1] != grid[row + i]:
                return False
    except:
        return True
def checkValidityCol(grid, col): # same as checkValidityRow but for columns
    try:
        for i in range(0, 999):
            assert (col - i - 1) >= 0 # negative indexing is a blessing and a curse
            if [row[col - i - 1] for row in grid] != [row[col + i] for row in grid]:
                return False
    except:
        return True
total = 0
for grid in text: # my code when i finished pt1 was significantly worse(including a check for the adj 2 columns when its covered by checkValidity funcs anyways), doing pt2 i refactored this so
    realGrid = grid.split('\n')
    realGrid = (realGrid if realGrid[-1] != '' else realGrid[:-1])
    for i in range(1, len(realGrid)):
        if (checkValidityRow(realGrid, i)):
            total += i * 100
    for col in range(1, len(realGrid[0])):
        if (checkValidityCol(realGrid, col)):
            total += col
print(total)
