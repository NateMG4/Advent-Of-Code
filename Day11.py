import copy


file = open('Data\Day11.txt', mode = "rt")
strings = file.readlines()
file.close()


class OctoMap:
    map = []
    cordList = []
    burstChart = []
    burstList = []
    bursts = 0
    def __init__(self, strings):
        self.generateMap(strings)
        self.cordList = self.buildCordList()
        self.burstChart = self.buildBurstChart()

    def generateMap(self, strings):
        for string in strings:
            temp = list(string.split("\n")[0])
            self.map.append(list(map(int, temp)))


    def get(self, cord = []):
        x = cord[0]
        y = cord[1]

        if(x < 0 or x >= len(self.map[0]) or y < 0 or y >= len(self.map)):
            return -1
        
        return self.map[y][x]


    def set(self, cord = [], value = ''):
        x = cord[0]
        y = cord[1]
        if(x < 0 or x>= len(self.map[0]) or y < 0 or y>= len(self.map) or value == ''):
            return -1
        self.map[y][x] = value

    def getBurst(self, cord):
        x = cord[0]
        y = cord[1]
        if(x < 0 or x >= len(self.map[0]) or y < 0 or y >= len(self.map)):
            return -1
        
        return self.burstChart[y][x]

    def setBurst(self, cord = [], value = ''):
        x = cord[0]
        y = cord[1]
        if(x < 0 or x>= len(self.map[0]) or y < 0 or y>= len(self.map) or value == ''):
            return -1
        self.burstChart[y][x] = value

    def buildCordList(self):
        list = []
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                list.append([x,y])
        return list


    def buildBurstChart(self):
        chart = []
        for y in range(len(self.map)):
            row = []
            for x in range(len(self.map[0])):
                row.append(False)
            chart.append(row)
        return chart


    def buildAdjacent(self, cord):
        x = cord[0]
        y = cord[1]
        adjcaent =[
            [x+1, y],
            [x-1,y],
            [x,y+1],
            [x,y-1],
            [x-1,y+1],
            [x+1,y-1],
            [x+1,y+1],
            [x-1,y-1],
        ]
        return adjcaent
    def increment(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                self.set([x,y], self.get([x,y]) + 1)
                if(self.get([x,y]) > 9):
                    self.burstList.append([x,y])
    def burst(self, cord):
        if(self.get(cord) != 0):
            self.set(cord, self.get(cord) + 1)
        value = self.get(cord)
        if(value > 9 and not self.getBurst(cord)):
            self.set(cord, 0)
            self.bursts += 1
            self.setBurst(cord, True)
            for c in self.buildAdjacent(cord):
                self.burst(c)
    def step(self):
        self.burstList = []
        self.increment()
        for cord in self.burstList:
            self.burst(cord)
        
        sync = True
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                value = self.get([x,y])
                if value != 0:
                    sync = False
                    break
            if not sync:
                break
        if(sync):
            return sync
        self.cordList = self.buildCordList()
        self.burstChart = self.buildBurstChart()


puzzleMap = OctoMap(strings)
#print(puzzleMap.cordList)


for step in range(0, 1000):
    print(f"Step# {step}")
    if(puzzleMap.step()):
        print(f"synched on step: {step+1}")
        break
    print(puzzleMap.bursts)
