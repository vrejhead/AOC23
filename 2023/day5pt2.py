import itertools, copy
with open('input.txt', 'r') as f:
    text = f.read().split('\n\n')

oldSeeds = list(map(int, text[0].split()[1:]))
seedRanges = list()
allMappings = list()
for i, item in enumerate(oldSeeds[::2]):
    seedRanges.append(range(item, item + oldSeeds[i * 2 + 1]))
for mapping in text[1:]:
    temp = mapping.split('\n')[1:]
    currentMappings = list()
    for item in temp:
        if item != '':
            ints = list(map(int, item.split()))
            currentMappings.append([range(ints[1], ints[1] + ints[2]), (ints[0] - ints[1])]) # [destination start, destination end, diff]
    allMappings.append(currentMappings)
def lookItUp(layerMapping, query):
    for (mappingRange, diff) in layerMapping:
        if query in mappingRange:
            return diff
    return 0
def rangeSplit(layerMapping, allSeedRange):
    allOutput = []
    for seedRange in allSeedRange:
        seedOutput = []
        splits = {seedRange.start, seedRange.stop}
        for (mappingRange, diff) in layerMapping:
            if (mappingRange.start in seedRange):
                splits.add(mappingRange.start)
            if (mappingRange.stop in seedRange):
                splits.add(mappingRange.stop + 1)
        splits = list(splits)
        splits.sort()
        for i in range(len(splits) - 1):
            seedOutput.append(range(splits[i] + lookItUp(layerMapping, splits[i]), splits[i + 1] + lookItUp(layerMapping, splits[i])))
        allOutput += seedOutput
    return allOutput
candidates = [99999999999]
for seedRange in seedRanges:
    currentSeedRange = copy.copy([seedRange])
    for i, layerMapping in enumerate(allMappings):
        currentSeedRange = rangeSplit(layerMapping, currentSeedRange)
    candidates.append(min(currentSeedRange, key=lambda x: x.start).start)
print(min(candidates))
