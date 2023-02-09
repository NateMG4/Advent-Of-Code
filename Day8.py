file = open('Data\Day8.txt', mode = "rt")
strings = file.readlines()
file.close()
keyString = "abcdefg"
segmentNumLegend = {
    2 : [1],
    3 : [7],
    4 : [4],
    5 : [2,3,5],
    6 : [0,6,9],
    7 : [8]
}
segmentLetterLegend = {
    "a" : [0,2,3,5,6,7,8,9],
    "b" : [0,4,5,6,8,9],
    "c" : [0,1,2,3,4,7,8,9],
    "d" : [2,3,4,5,6,8,9],
    "e" : [0,2,6,8,],
    "f" : [0,1,3,4,5,6,7,8,9],
    "g" : [0,2,3,5,6,8,9],
}
sortedPatterns = {
    0 : "abcefg",
    1 : "cf",
    2 : "acdeg",
    3 : "acdfg",
    4 : "bcdf",
    5 : "abdfg",
    6 : "abdefg",
    7 : "acf",
    8 : "abcdefg",
    9 : "abcdfg"
}



def filter(arg1, arg2):
    x = ""
    for i in keyString:
        if(i in arg1 and i in arg2):
            x += i
    return x
def removeSimilar(arg1, arg2):
    x = ""
    for i in arg1:
        if(i in arg1 and i in arg2):
            continue
        x += i
    return x

def partialTranslation(num):
    x = set()
    sp = sortedPatterns[num]
    for letter in sp:
        x.add(set(translationGuide[letter]))
    return setToString(x)
def setToString(s):
    string = ""
    for x in s:
        string += x
    return string

number = 0
index = 0
for string in strings:
    translationGuide = {
        "a" : "abcdefg",
        "b" : "abcdefg",
        "c" : "abcdefg",
        "d" : "abcdefg",
        "e" : "abcdefg",
        "f" : "abcdefg",
        "g" : "abcdefg",
    }
    index += 1
    patternToNumber = dict()
    args = string.split(" | ")
    testPatterns = args[0]
    outputPatterns = args[1].split("\n")[0].split(" ")

    patterns = testPatterns.split(" ")
    patterns.sort(key=len)
    #print("Patterns: " + str(patterns))
    remainingPatterns = [[],[]]


    for p in patterns:
        possible = segmentNumLegend[len(p)]
        #print(p + ": " + str(possible))
        if(len(possible) != 1):
            remainingPatterns[len(p)%2].append(p)
            continue
        patternToNumber[p] = possible[0]
        for digit in possible:
            sortedPattern = sortedPatterns[digit]
            for letter in sortedPattern:
                translationGuide[letter] = filter(translationGuide[letter], p)
            for letter in removeSimilar(keyString, sortedPattern):
                translationGuide[letter] = removeSimilar(translationGuide[letter], p)
    
    for x in translationGuide:
        print(x + ": " + translationGuide[x])

    pairs = ["bd", "eg", "cf"]
    pairTranslation = dict()
    pairTranslation["bd"] = translationGuide["b"]
    pairTranslation["eg"] = translationGuide["e"]
    pairTranslation["cf"] = translationGuide["c"]

    print(pairs)

    guide = {
    "bd" : 0,   
    "eg" : 9,
    "cf" : 6,
    }
    # 0,6,9
    for p in remainingPatterns[0]:
        for pair in pairs:
            if(len(filter(pairTranslation[pair], p)) == 1):
                patternToNumber[p] = guide[pair]
    guide = {
    "bd" : 5,   
    "eg" : 2,
    "cf" : 3,
    }
    # 2,3,5
    for p in remainingPatterns[1]:
        for pair in pairs:
            if(len(filter(pairTranslation[pair], p)) == 2):
                patternToNumber[p] = guide[pair]
    print(patternToNumber)
    outputString = ""
    for p in outputPatterns:
        for comp in patternToNumber.keys():
            if set(comp) == set(p):
                outputString += str(patternToNumber[comp])
    number += int(outputString)
print(number)
"""
print(patternToNumber)
print("Remaining patterns: " + str(remainingPatterns))

"""




    
"""

for a in pairs.keys():
    b = pairs.get(a)
    exclusive = list(set(segmentLetterLegend[a]) - set(segmentLetterLegend[b]))
    print("{}, {}: {}".format(a, b, exclusive))




print(numDig)


for i in range(9):
    print(str(i) + " : " + partialTranslation(i))


for p in remainingPatterns:
    possible = segmentLegend[len(p)]
    print()
    print(p + ": " + str(possible))
    removeLetters = "abcdefg"
    for digit in possible:
        part = partialTranslation(digit)
        print(str(digit) + " : " + part + " : " +  removeSimilar(part, p))
        removeLetters = filter(removeLetters, removeSimilar(part, p))
    sortedPattern = sortedPatterns[digit]
    for letter in removeSimilar(keyString, sortedPattern):
        translationGuide[letter] = removeSimilar(translationGuide[letter], removeLetters)
"""
