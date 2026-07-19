

file = open('Data\Day3.txt', mode = "rt")
strings = file.readlines()
file.close()

numBits = []

def binaryToDecimal(val): 
    return int(val, 2) 

def findLastByte(bitIndex, vaildBytes, inverted):
    bitList = findBitList(vaildBytes)
    comparison = findMostCommon(bitList[bitIndex], inverted)
    newVaild = []
    for v in vaildBytes:
        if(comparison == int(v[bitIndex])):
            newVaild.append(v)

    length = len(newVaild)
    if(len(newVaild) <= 1):
        return newVaild[0]
    else:
        return findLastByte(bitIndex + 1, newVaild, inverted)

def findMostCommon(array, inverted):
    num = 0
    length = (len(array) / 2)
    for bit in array:
        num += int(bit)
    var = num >= length
    if inverted:
        return int(not var)
    else:
        return int(var)

def partTwo():
    numBytes = len(strings)
    vaildBytes = []
    bitList = []

    for x in range(12):
        numBits.append(0)
        bitList.append([])

    for string in strings:
        args = string.split("\n")
        vaildBytes.append(args[0])

    o = binaryToDecimal(findLastByte(0, vaildBytes, False))
    c = binaryToDecimal(findLastByte(0, vaildBytes, True))
    print(o)
    print(c)
    print(o * c)


def findBitList(array):
    bitList = []

    for x in range(12):
        bitList.append([])

    for byte in array:
        i = 0
        bits = [*byte[0]]
        for bit in byte:
            bitList[i].append(bit)
            i += 1
    return bitList
    # i = 0
    # oxygen = ''
    # co2 = ''

    # for bit in numBits:
    #     var = bit >= (numBytes/2)
    #     oxygen += str(int(var))
    #     co2 += str(int(not var))
    #     i += 1
    
    # oxygenDecimal = findLastByte(0, vaildBytes, oxygen)
    # co2Decimal = findLastByte(0, vaildBytes, co2)
    # print(oxygenDecimal) 
    # print(co2Decimal)

    # print(binaryToDecimal(findLastByte(0, vaildBytes, oxygen)) * binaryToDecimal(findLastByte(0, vaildBytes, co2)))
    

def partOne():

    numBits = []
    gammaRate = []
    numBytes = len(strings)

    for x in range(12):
        numBits.append(0)
        gammaRate.append(0)


    for string in strings:
        args = string.split("\n")
        i = 0
        bits = [*args[0]]
        for bit in bits:
            numBits[i] += int(bit)
            i += 1

    i = 0
    for bit in numBits:
        gammaRate[i] = bit > (numBytes/2)
        i += 1


    epsilonRate = []
    for g in gammaRate:
        epsilonRate.append(not g)

    eNum = ""
    gNum = ""
    for x in range(12):
        gNum += str(int(gammaRate[x]))
        eNum += str(int(epsilonRate[x]))
    
    print(gNum)
    print(eNum)
    print(binaryToDecimal(gNum) * binaryToDecimal(eNum))


partTwo()
