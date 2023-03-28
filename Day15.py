import heapq
import math
import sys

file = open('Data\Day15.txt', mode = "rt")
strings = file.readlines()
file.close()

grid = []


for line in strings:
    line = list(line.split("\n")[0])
    grid.append(line)

maxX = len(grid[0])
maxY = len(grid)
maxExtendedX = maxX * 5
maxExtendedY = maxY* 5


def findNeighbors(point, max_x, max_y):
    x = point[0]
    y = point[1]

    adjcaent = set([
        (min(x+1,max_x-1), y),
        (max(x-1,0),y),
        (x,min(y+1,max_y-1)),
        (x,max(y-1,0))
    ])

    return adjcaent

def get(point, g = grid):
    largest_axis = max(point[1], point[0])
    realative_cord = (point[0] % maxX, point[1] % maxY)
    add = (point[1] // maxX) + (point[0] // maxY)
    #if(add != 0):
        #print()

    calculated_value = int(g[realative_cord[1]][realative_cord[0]]) + add
    calculated_value =  calculated_value % 9 if calculated_value > 9 else calculated_value
    return int(calculated_value)



def getRiskGrid(point):
    return int(riskGrid[point[1]][point[0]])

"""
def getRiskGrid2(point):
    return int(riskGrid2[point[1]][point[0]])
def tracePathToStart2(point, p = []):
    p.append(point)
    if(point == (0,0)):
        return p
    neighbors = list(findNeighbors(point))  
    neighbors.sort(key=getRiskGrid2)
    tracePathToStart2(neighbors[0], p)
    return p
"""
def tracePathToStart(point, p = []):
    p.append(point)
    if(point == (0,0)):
        return p
    neighbors = list(findNeighbors(point, maxExtendedX, maxExtendedY))  
    neighbors.sort(key=getRiskGrid)
    tracePathToStart(neighbors[0], p)
    return p


def sumPath(path):
    sum = 0
    for p in path:
        sum += int(grid[p[1]][p[0]])
    return sum
def printRiskGrid():
    for row in riskGrid:
        for value in row:
            print(value, end=" ")
        print()

def printGrid(p):
    for y in range(maxExtendedY):
        for x in range(maxExtendedX):
            if((x,y) in p):
                print(get((x,y)), end=" ")
                continue
            print(".", end = " ")
        print()

def createRiskGrid(grid, xMult, yMult):
    riskGrid = []
    for y in range(len(grid) * yMult):
        row = []
        for x in range(len(grid[0]) * xMult):
            row.append(math.inf)
        riskGrid.append(row)
    riskGrid[0][0] = 0
    return riskGrid

riskGrid = createRiskGrid(grid,5,5)


def DijkstraTest1():


    visited = []
    queue = [(0,0)]


    numElements = maxX * maxY
    nextQueue = list()

    while(len(queue) > 0):
        nextQueue = []

        for point in queue:

            neighbors = findNeighbors(point, maxExtendedX, maxExtendedY)
            for n in neighbors:

                if(point == n):
                    continue

                newDist = getRiskGrid(point) + get(n)
                currentDist = riskGrid[n[1]][n[0]]
                if(newDist < currentDist):
                    nextQueue.append(n)
                    riskGrid[n[1]][n[0]] = newDist

            visited.append(point)
        #displayGrid.changeText(queue, riskGrid)
        #win.getMouse()

        queue = nextQueue
    print(riskGrid[maxExtendedY-1][maxExtendedX-1])

def DijkstraTest2(data):

    shortestDistance = {(0,0): 0}
    visited = {}
    previousNode = {}

    heap = []
    heapq.heappush(heap, (0, (0,0)))

    while len(heap) > 0:
        
        distance, point = heapq.heappop(heap)
        x, y = point
        visited[point] = True

        # get all adjacent neighors 
        neighbors =  [ (x+dx, y+dy) for dx,dy in [(0,-1),(-1,0),(0,1),(1,0)] ]
        
        # that are not out of bounds
        neighbors = [ (x,y) for x,y in neighbors if x >= 0 and x < maxExtendedX and y >= 0 and y < maxExtendedY] 
        # and not already visited
        neighbors = [ neighbor for neighbor in neighbors if neighbor not in visited ]

        if shortestDistance[point] < distance:
            continue

        for neighbor in neighbors:

            neighborX, neighborY = neighbor
            riskLevel = get((neighborX,neighborY))
            newDistance = shortestDistance[point] + riskLevel

            if neighbor not in shortestDistance or newDistance < shortestDistance[neighbor]:
                shortestDistance[neighbor] = newDistance
                previousNode[neighbor] = point
                heapq.heappush(heap, (newDistance, neighbor))
                riskGrid[neighbor[1]][neighbor[0]] = newDistance
            

    print(previousNode[(len(data[0])-1,len(data)-1)])
    return shortestDistance[(maxExtendedX-1,maxExtendedY-1)]


"""
riskGrid2 = []
for y in range(len(grid)):
    row = []
    for x in range(len(grid[0])):
        row.append(math.inf)
    riskGrid2.append(row)
riskGrid2[0][0] = 0
def DijkstraTest2(data):

    shortestDistance = {(0,0): 0}
    visited = {}
    previousNode = {}

    heap = []
    heapq.heappush(heap, (0, (0,0)))

    while len(heap) > 0:
        
        distance, point = heapq.heappop(heap)
        x, y = point
        visited[point] = True

        # get all adjacent neighors 
        neighbors =  [ (x+dx, y+dy) for dx,dy in [(0,-1),(-1,0),(0,1),(1,0)] ]
        
        # that are not out of bounds
        neighbors = [ (x,y) for x,y in neighbors if x >= 0 and x < len(data[0]) and y >= 0 and y < len(data)] 
        # and not already visited
        neighbors = [ neighbor for neighbor in neighbors if neighbor not in visited ]

        if shortestDistance[point] < distance:
            continue

        for neighbor in neighbors:

            neighborX, neighborY = neighbor
            riskLevel = int(data[neighborY][neighborX])
            newDistance = shortestDistance[point] + riskLevel

            if neighbor not in shortestDistance or newDistance < shortestDistance[neighbor]:
                shortestDistance[neighbor] = newDistance
                previousNode[neighbor] = point
                heapq.heappush(heap, (newDistance, neighbor))
                riskGrid2[neighbor[1]][neighbor[0]] = newDistance
            

    print(previousNode[(len(data[0])-1,len(data)-1)])
    return shortestDistance[(len(data[0])-1,len(data)-1)]
"""

print(get((99,99)))
print(get((199, 199)))
print(get((299, 299)))
print(get((399, 399)))
print(get((499, 499)))
print(get((599, 599)))
print(get((699, 699)))


print(DijkstraTest2(grid))






DijkstraTest1()


#print(getRiskGrid((499, 499)))

"""
print(DijkstraTest2(grid))
stdoutOrigin=sys.stdout 
sys.stdout = open("log2.txt", "w"))
path2 = tracePathToStart2((maxX-1, maxY-1), p = [])

sys.stdout.close()
sys.stdout=stdoutOrigin
"""

# Print text to the terminal, adding color
# color is a number from 0 to 7:
# 0: gray    1: red     2: green    3: yellow
# 4: blue    5: magenta 6: cyan     7: white
def colorPrint(color, text, eol = False):
  prefix = "\033[3" + str(color) + "m" # escape + color code
  suffix = "\033[0m"  # reset code

  print(prefix + str(text) + suffix, end='\n' if eol else "")
"""

cords = []
def printDifference(path1, path2):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            spaces = (5 - len(str(riskGrid[y][x])))*" "
            if((x,y) in path1 and (x,y) in path2):
                colorPrint(7 , riskGrid2[y][x])
                
                print("", end=spaces)
                continue
            elif (x,y) in path1:
                colorPrint(2 , riskGrid2[y][x])
                print("", end=spaces)

                continue
            elif (x,y) in path2:
                cords.append((x,y))

                colorPrint(1 , riskGrid2[y][x])
                print("", end=spaces)

                continue
            colorPrint(0 , riskGrid2[y][x])
            print("", end=spaces)

        print()

printDifference(path1,path2)
print(f"\n\n\n\n{cords}")
"""






