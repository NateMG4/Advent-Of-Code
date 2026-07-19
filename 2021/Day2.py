
file = open('Data\Day2.txt', mode = "rt")
strings = file.readlines()
file.close()

depth = 0
dist = 0
aim = 0

for string in strings:
    args = string.split()
    value = int(args[1])
    if args[0] == 'forward':
        dist += value
        depth += value*aim
    elif args[0] == 'down':
        aim += value
    elif args[0] == 'up':
        aim -= value
print(depth)
print(dist)
print(dist * depth)