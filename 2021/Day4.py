from xml.dom.expatbuilder import parseString


file = open('Data\Day4.txt', mode = "rt")
strings = file.read().split("\n\n")
file.close()

def partOne():
    drawnNumbers = strings.pop(0).split(",")
    grids = []
    for s in strings:
        var = Grid(s)
        grids.append(var)
    print()

    for num in drawnNumbers:
        for g in grids:
            var = g.contains(num)
            if(var != -1):
                return var
            
def partTwo():
    drawnNumbers = strings.pop(0).split(",")
    grids = []
    winners = []
    for s in strings:
        var = Grid(s)
        grids.append(var)
    print()

    i = 0
    for num in drawnNumbers:
        if len(grids) <= 0:
            break
        removeGrids = []
        for g in grids:
            var = g.contains(num)
            if(var != -1):
                winners.append(var)
                removeGrids.append(g)
        for r in removeGrids:
            grids.remove(r)
        i += 1
    return winners.pop()
    
class Grid:

    def __init__(self, string) -> None:
        self.gridValues = [[], [], [], [], []]
        self.row = [0, 0, 0, 0, 0]
        self.col = [0, 0, 0, 0, 0]
        self.selected = []
        self.nonSelected = []
        self.parseStringToGrid(string)
        pass


    def parseStringToGrid(self, string):
        lines = string.split("\n")
        i = 0
        for line in lines:
            args = line.split(" ")
            for a in args:
                if(a != ""):
                    self.gridValues[i].append(a)
                    self.nonSelected.append(a)
            i += 1
                
    def contains(self, value):
        for r in range(5):
            for c in range(5):
                if(self.gridValues[r][c] == value):
                    self.selected.append(value)
                    self.nonSelected.remove(value)
                    self.row[r] += 1
                    self.col[c] += 1
                    if self.row[r] >= 5 or self.col[c] >= 5:
                        return self.calulateNon() * int(value)
        return -1
    
    def calulateNon(self):
        var = 0
        for num in self.nonSelected:
            var += int(num)
        return var


print(partTwo())