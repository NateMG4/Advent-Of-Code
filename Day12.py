file = open('Data\Day12.txt', mode = "rt")
strings = file.readlines()
file.close()



class Node():


    def __init__(self, name = "", p = [], bigCave = False):
        self.bigCave = bigCave
        self.name = name

        self.parents = []
        self.children = []

        self.parents += p
        for n in self.parents:
            n.children.append(self)

    def addParent(self, parent):
        if(parent not in self.parents):
            self.parents.append(parent)
        if(self not in parent.children):
            parent.children.append(self)
    def printChildren(self, depth = 0):
        print(f"{self.name}")
        for c in self.children:
            print(c.name, end=" ")
        print("\n---\n")

nodes = dict()
for line in strings:
    line = line.split("\n")[0]
    newNodes = line.split("-")
    
    keys = nodes.keys()

    name = newNodes[0]
    parent = nodes[newNodes[0]] if newNodes[0] in keys else Node(name, bigCave=name.isupper())


    name = newNodes[1]
    if newNodes[1] in keys:
        child = nodes[newNodes[1]]
        child.addParent(parent)
    else:
        child = Node(name, [parent], bigCave=name.isupper())

    for n in [parent, child]:
        if(n.name not in nodes.keys()):
            nodes[n.name] = n

paths = []
def findPathToEndFrom(node, prevSteps = []):
    path = prevSteps + [node.name]

    if(node.name == "end"):
        paths.append(path)
        return
    adjNodes = node.parents + node.children
    filtered = []
    print()
    printPath(path)
    for n in adjNodes:
        if n.name not in path or (n.name in path and n.name.isupper()):
            print(n.name, end=" ")
            filtered.append(n)
    for n in filtered:
        print(f"\nChoice: {n.name}")
        findPathToEndFrom(n, path)

def findPathToEndFromPart2(node, prevSteps = [], doubleSmall=False):
    if(not doubleSmall):
        doubleSmall = node.name in prevSteps and not node.name.isupper()

    path = prevSteps + [node.name]
    if(node.name == "end"):
        paths.append(path)
        return
    adjNodes = node.parents + node.children
    filtered = []
    #print()
    #printPath(path)
    #print(f"Double Small: {doubleSmall}")

    for n in adjNodes:
        if (n.name not in path or (not doubleSmall or (n.name in path and n.name.isupper()))) and n.name != 'start':
            #print(n.name, end=" ")
            filtered.append(n)
    for n in filtered:
        #print(f"\nChoice: {n.name}")
        findPathToEndFromPart2(n, path, doubleSmall)

def printPath(path):
    for i in range(len(path)-1):
        print(path[i], end="->")
    print(path[-1])

#for k in nodes:
    #nodes[k].printChildren()
findPathToEndFromPart2(nodes["start"])
#for p in paths:
 #   printPath(p)
print(len(paths))