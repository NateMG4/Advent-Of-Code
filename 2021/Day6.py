file = open('Data\Day6.txt', mode = "rt")
strings = file.read()
file.close()

def grow(laternFish):
    new = laternFish.pop(0)
    laternFish.append(new)
    laternFish[6] += new

    return laternFish

def partOne():

    values = list(map(int, strings.split(",")))
    values.sort()
    compare = 1
    laternFish = [0, 0]
    index = 0
    for i in range(len(values)):
        if values[i] != compare:
            index = i
            laternFish.append(0)
            compare += 1
        laternFish[compare] = i - index + 1
    laternFish.append(0)
    laternFish.append(0)
    laternFish.append(0)


    for i in range(256):
        laternFish = grow(laternFish)
    var = 0
    for i in laternFish:
        var += i
    print(var)

partOne()