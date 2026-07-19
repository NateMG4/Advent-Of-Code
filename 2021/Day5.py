file = open('Data\Day5.txt', mode = "rt")
strings = file.read().splitlines()
file.close()

def partOne():

    lines = []
    intMap = {}
    for string in strings:
        args = string.split(" -> ")
        parts1 = args[0].split(",")
        parts2 = args[1].split(",")
        line = (Line(Point(parts1[0], parts1[1]), Point(parts2[0], parts2[1])))
        if(line.vertical or line.horizontal or line.diagonal):
            lines.append(line)
    for line in lines:
        intersections = line.intersect()
        for i in intersections:
            if intMap.get(i.toString(), -1) == -1:
                intMap[i.toString()] = 1
            else:
                intMap[i.toString()] += 1
    var = 0
    for i in intMap:
        if intMap[i] >= 2:
            var += 1

    print(var)
class Point:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        
    def toString(self):
        return str(self.x) + "," + str(self.y)
class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.vertical = p1.x == p2.x
        self.horizontal = p1.y == p2.y
        if self.p1.x != self.p2.x and self.p1.y != self.p2.y:
            self.diagonal = (abs(p2.y - p1.y) / abs(p2.x - p1.x)) == 1
    
    def intersect(self):
        intersectionPoints = []
        r = 0
        if self.vertical:
            r = abs(self.p2.y - self.p1.y)
            dx = 0
            dy = 1
            point = Point(self.p1.x, min(self.p1.y, self.p2.y))

        elif self.horizontal:
            r = abs(self.p2.x - self.p1.x)
            dx = 1
            dy = 0
            point = Point(min(self.p1.x, self.p2.x), self.p1.y)
        elif self.diagonal:
            r = abs(self.p2.x - self.p1.x)
            if self.p2.x - self.p1.x > 0:
                dx = 1
            else:
                dx = -1
            if self.p2.y - self.p1.y > 0:
                dy = 1
            else:
                dy = -1
            point = self.p1
        for i in range(r + 1):
            var = Point(point.x + (i * dx), point.y + (i * dy))
            intersectionPoints.append(var)
        return intersectionPoints


        





partOne()
