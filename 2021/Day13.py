file = open('Data\Day13.txt', mode = "rt")
strings = file.readlines()
file.close()


class Point():
    def __init__(self, x, y) -> None:
        self.setPoint(x,y)
    def setPoint(self,x,y):
        self.x = x
        self.y = y


def createGrid(mp):
    grid = []
    for y in range(mp.y + 1):
        grid.append([])
        for x in range(mp.x + 1):
            grid[y].append(0)
    return grid

points = []
index = 0
maxPoint = Point(0, 0)
# Points
for line in strings:
    if(line == "\n"):
        break
    line = line.split("\n")[0].split(',')
    p = Point(int(line[0]),int(line[1]))
    points.append(p)
    maxPoint.setPoint(max(p.x, maxPoint.x), max(p.y, maxPoint.y))
    index += 1


foldLines = strings[index+1::]
print(f"maxPoint: {maxPoint.x} {maxPoint.y}")
grid = createGrid(maxPoint)


def gridSet(p, value):
    grid[p.y][p.x] = value
def gridPrint(grid):
    for row in grid:
        for i in row:
            if(i == 1):
                print("#", end=" ")
                continue
            print(".", end=" ")

        print()
    

for p in points:
    gridSet(p, 1)

#gridPrint(grid)

def foldGrid(axis, n):

    if(axis == 'y'):
        for y in range(n, len(grid)):
            for x in range(0, len(grid[0])):
                if(grid[y][x] == 1):
                    mirrorPoint = Point(x, n - (y-n))
                    gridSet(mirrorPoint, 1)
        return grid[:n]
    else:
        for y in range(0, len(grid)):
            for x in range(n, len(grid[0])):
                if(grid[y][x] == 1):
                    mirrorPoint = Point( n - (x-n),y)
                    gridSet(mirrorPoint, 1)
        newGrid = []
        for row in grid:
            newGrid.append(row[:n])
        return newGrid
# Folds
def printNumPoints(grid):
    num = 0
    for row in grid:
        for i in row:
            if(i == 1):
                num += 1

    print(num)

for line in foldLines:
    line = line.split("\n")[0].split(" ")[-1].split("=")
    axis = line[0]
    n = int(line[1])
    print(f"{axis}={n}")

    grid = foldGrid(axis,n)
    gridPrint(grid)
    printNumPoints(grid)

gridPrint(grid)



