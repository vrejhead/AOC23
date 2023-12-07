import itertools
with open('temp0.txt', 'r') as f:
    text = f.read().split('\n\n')

seeds = list(map(int, text[0].split()[1:]))
# for i, item in enumerate(oldSeeds[::2]):
#     seeds.append(range(item, item + oldSeeds[i * 2 + 1]))
allMappings = []
def convert(mapping, seed):
    for item in mapping:
        if ((item[0] <= seed) and (seed < item[1])):
            return seed - item[2]
    return seed
for mapping in text[1:]:
    lines = mapping.split('\n')
    temp = list()
    for line in lines[1:]:
        if line != '':
            ints = list(map(int, line.split()))
            temp.append([ints[1], ints[1] + ints[2], (ints[1] - ints[0])])
    allMappings.append(temp)
for mapping in allMappings:
    for i, seed in enumerate(seeds):
        seeds[i] = convert(mapping, seed)
print(min(seeds))
