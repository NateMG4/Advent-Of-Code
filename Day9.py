import copy


file = open('Data\Day9.txt', mode = "rt")
strings = file.readlines()
file.close()

heightMap = []
index = 0
for string in strings:
    array = list(string.split("\n")[0])
    heightMap.append(array)
#print(heightMap)

def partOne():
    lowestCords = []
    for y in range(0, len(heightMap)):
        for x in range(0, len(heightMap[y])):
            adjacent = [
            [x, y-1],
            [x, y+1],
            [x-1, y],
            [x+1, y]
            ]   
            if localEval(x,y, adjacent):
                lowestCords.append([x,y])
            
    print(lowestCords)
    print()

    totalRisk = 0
    for cord in lowestCords:
        risk = 1 + int(heightMap[cord[1]][cord[0]])
        totalRisk+=risk
    print(totalRisk)

def partTwo():
    lowestCords = []
    for y in range(0, len(heightMap)):
            for x in range(0, len(heightMap[y])):
                compareValue = heightMap[y][x]
                adjacent = [
                [x, y-1],
                [x, y+1],
                [x-1, y],
                [x+1, y]
                ]   
                if localEval(x,y, adjacent):
                    lowestCords.append([x,y])
    #print(lowestCords)
    basinList = []

    for cord in lowestCords:
        basinList.append(basinToSet(basinEval(cord,[],[], cord)))
        #print("Basin Size: " + str(len(basinList[-1])))
        #buildLocalMap(basinList[-1], first=cord)

    print("\n ---Final--- \n")
    basinList.sort(reverse=True, key=len)

    """
    for i in range(0,3):
        basin = basinList[i]
        buildLocalMap(basin)
        print("Basin Size: " + str(len(basin)))
        setBasin = basinToSet(basin)
        print("Basin Set Size: " + str(len(setBasin)))

        #printBasinValues(basin)
    """

    print()
    print("Final: " + str(len(basinList[0]) * len(basinList[1]) * len(basinList[2]))) 

def basinToSet(basin):
    newSet = set()
    for cord in basin:
        x = cord[0]
        y = cord[1]
        string = "{}, {}".format(x,y)
        newSet.add(string)
    return newSet
def basinEval(target, previous, basin, first):
    adjacent = []
    x = target[0]
    y = target[1]
    
    basin.append(target)


    if y-1 >= 0:
        adjacent.append([x, y-1])
    if y+1 < len(heightMap):
        adjacent.append([x, y+1])
    if x-1 >= 0:
        adjacent.append([x-1, y])
    if x+1 < len(heightMap[0]):
        adjacent.append([x+1, y])

    # look at all adjacent cords, if search only the ones that are not in the basin and are less than 9
    testCases = []
    for cord in adjacent:
        cordValue = heightMap[cord[1]][cord[0]]
        inBasin = cord in basin
        if(inBasin or cordValue == '9'):
            continue
        testCases.append(cord)

    print(buildLocalMap(basin, testCases, target, previous, first))
    print()

    for cord in testCases:    
        basinEval(cord, target, basin, first)
    return basin

def buildLocalMap(basin, testCases = [], current = [], previous=[], first = []):
    localList = []
    localList += basin
    localList.append(previous)
    localList += testCases
    localList.append(current)
    localList = [i for i in localList if i != []]

    topLeftCord = copy.copy(localList[0])
    topRightCord = copy.copy(localList[-1])

    for cord in localList:

        topLeftCord[0] = min(topLeftCord[0], cord[0])
        topLeftCord[1] = min(topLeftCord[1], cord[1])
        topRightCord[0] = max(topRightCord[0], cord[0])
        topRightCord[1] = max(topRightCord[1], cord[1])

    topLeftCord[0] = max(topLeftCord[0] - 1, 0)
    topLeftCord[1] = max(topLeftCord[1] - 1, 0)
    topRightCord[0] = min(topRightCord[0] + 1, len(heightMap[0]))
    topRightCord[1] = min(topRightCord[1] + 1, len(heightMap))

    map = []
    for y in range(topLeftCord[1],min(topRightCord[1]+1, len(heightMap))):
        temp = []
        for x in range(topLeftCord[0],min(topRightCord[0]+1, len(heightMap[0]))):
            temp.append(heightMap[y][x])
        map.append(temp)
    printBasin(basin, testCases, current, previous, map, topLeftCord, first)


def printBasin(basin, testCases = [], current = [], previous=[], map = heightMap, topLeft = [0,0], first = []):
   # print("topLeft "  + str(topLeft))
    #print("MapX: " + str(len(map[0])) + "\nMapY: " + str(len(map)))
    #print()
    
    for y in range(0, len(map)):
            index = y
            y += topLeft[1]

            for x in range(0, len(map[index])):
                
                x += topLeft[0]

                val = heightMap[y][x]
                addString = val
                if([x,y] in basin):
                    addString = ""
                    if val == 9:
                        addString = "!"
                        
                if([x,y] in testCases):
                    addString += "$"
                if [x,y] == current:
                    addString = "@"
                if [x,y] == first:
                    addString = "*"
                spaces = ""
                for i in range(0, 4-(len(addString))):
                    spaces += " "
                print(addString, end=spaces)
            print()
def printBasinValues(basin):
    for cord in basin:
        print("{}: {}".format(cord, heightMap[cord[1]][cord[0]]))


def localEval(x, y, evalList):
    compareValue = heightMap[y][x]
    lowest = True
    for cord in evalList:
        if cord[0] >= len(heightMap[y]) or cord[0] < 0 or cord[1] >= len(heightMap) or cord[1] < 0:
            continue
        if min(compareValue, heightMap[cord[1]][cord[0]]) != compareValue or compareValue == heightMap[cord[1]][cord[0]]:
            return False
    return lowest

partTwo()