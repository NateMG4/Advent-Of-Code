file = open('Data\Day7.txt', mode = "rt")
strings = file.read()
file.close()

values = list(map(int, strings.split(",")))
values.sort()


def calculateFuel(index):
    dist = 0
    for i in range(len(crabs)):
        if(i != index):
            d = abs(index - i)
            dist += int((d * (d+1))/2) * crabs[i]
    return dist

print()
compare = 0
crabs = [0] * (values[-1] + 1)
index = 0
for i in range(len(values)):
    if values[i] != compare:
        index = i
        compare = values[i]
    crabs[compare] = i - index + 1

fuel = []
for i in range(len(crabs)):
    fuel.append(calculateFuel(i))
fuel.sort()
print(fuel[0])