isPart2 = False
with open(r'input.txt', 'r') as f:
    text = map(lambda x: x[:-1], f.readlines())
mapping = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
if isPart2:
    mapping = {'one': 1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
def temp4(string):
    output = []
    for item in mapping.items():
        if (temp := string.find(item[0])) != -1:
            output.append((item[1], temp))
    out = str(min(output, key=lambda x: x[1])[0])
    output.clear()
    string = string[::-1]
    for item in mapping.items():
        if (temp := string.find(item[0][::-1])) != -1:
            output.append((item[1], temp))
    out += str(min(output, key=lambda x: x[1])[0])
    return out
text3 = map(int, (map(temp4, text)))
print(sum(text3))
