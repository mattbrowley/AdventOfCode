from pathlib import Path

folderName = Path(__file__).parent.resolve()
inputFilename = Path(folderName, "Input5.txt")
with open(inputFilename, "r") as f:
    lines = f.read().splitlines()
vents = []
for line in lines:
    point1, point2 = line.split(" -> ")
    x1, y1 = point1.split(",")
    x2, y2 = point2.split(",")
    vents.append([[int(x1), int(y1)], [int(x2), int(y2)]])

map = []
for i in range(1000):
    newRow = []
    for j in range(1000):
        newRow.append(0)
    map.append(newRow)

# Part 1
for vent in vents:
    if vent[0][0] == vent[1][0]:
        x = vent[0][0]
        # print(f"Horizontal on {x}")
        lower = min(vent[0][1], vent[1][1])
        upper = max(vent[0][1], vent[1][1])
        for y in range(lower, upper + 1):
            map[x][y] += 1
    elif vent[0][1] == vent[1][1]:
        y = vent[0][1]
        # print(f"Vertical on {y}")
        lower = min(vent[0][0], vent[1][0])
        upper = max(vent[0][0], vent[1][0])
        for x in range(lower, upper + 1):
            map[x][y] += 1

intersections = 0
for row in map:
    for point in row:
        if point >= 2:
            intersections += 1
print("Part 1")
print("======")
print(f"Number of peaks: {intersections}")

# Part 2
for vent in vents:
    if vent[0][0] < vent[1][0] and vent[0][1] < vent[1][1]:
        xstart = vent[0][0]
        ystart = vent[0][1]
        xdiff = vent[1][0] - vent[0][0]
        for i in range(xdiff + 1):
            map[xstart + i][ystart + i] += 1
    elif vent[0][0] > vent[1][0] and vent[0][1] > vent[1][1]:
        xstart = vent[1][0]
        ystart = vent[1][1]
        xdiff = vent[0][0] - vent[1][0]
        for i in range(xdiff + 1):
            map[xstart + i][ystart + i] += 1
    if vent[0][0] < vent[1][0] and vent[0][1] > vent[1][1]:
        xstart = vent[0][0]
        ystart = vent[0][1]
        xdiff = vent[1][0] - vent[0][0]
        for i in range(xdiff + 1):
            map[xstart + i][ystart - i] += 1
    if vent[0][0] > vent[1][0] and vent[0][1] < vent[1][1]:
        xstart = vent[1][0]
        ystart = vent[1][1]
        xdiff = vent[0][0] - vent[1][0]
        for i in range(xdiff + 1):
            map[xstart + i][ystart - i] += 1

intersections = 0
for row in map:
    for point in row:
        if point >= 2:
            intersections += 1
print("Part 2")
print("======")
print(f"Number of peaks: {intersections}")
