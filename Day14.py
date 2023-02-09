from collections import defaultdict
import copy
import math


file = open('Data\Day14.txt', mode = "rt")
strings = file.readlines()
file.close()


def insertAt(array, i, add):
    left = array[:i+1]
    right = array[i+1:]
    return left  + add + right

def stringToPairs(string):
    string = list(string)
    pairs = dict()
    for i in range(len(string) - 1):
        pairs[string[i] + string[i+1]] = 1
    return pairs

startingPolymer = list(strings[0][:-1])


rules = dict()
for line in strings[2:]:
    rule = line.split("\n")[0].split(" -> ")
    rules[rule[0]] = rule[1]


polymerPairs = defaultdict(int)
polymerPairs.update(stringToPairs(startingPolymer))
steps= 40
for i in range(steps):
    newPolymer = copy.copy(polymerPairs)
    for pair in polymerPairs:
        if pair in rules and polymerPairs[pair] != 0:
            numTimes = polymerPairs[pair]
            insert = rules[pair]
            newPolymer[pair] -= 1 * numTimes
            newPolymer[pair[0] + insert] += 1 * numTimes
            newPolymer[insert + pair[1]] += 1 * numTimes
    polymerPairs = copy.copy(newPolymer)
    numPairs = sum(polymerPairs.values())
    desiredNumPairs = 3 * (2 ** (i+1))
    print(f"Number of calculated pairs: {numPairs} \nNumber of pairs we should have: {desiredNumPairs}")


frequency = defaultdict(int)


for pair in polymerPairs:
    num = polymerPairs[pair]
    frequency[pair[0]] += 1 * num
    frequency[pair[1]] += 1 * num
for l in frequency:
    frequency[l] = math.ceil(frequency[l] / 2)


print(max(frequency.values())- min(frequency.values()))
