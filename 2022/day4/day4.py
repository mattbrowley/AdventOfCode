import numpy as np

with open("day4data.txt", "r") as f:
    lines = f.readlines()
    numGroups = len(lines)
    groups = np.empty([numGroups, 2], dtype=object)
    for i, line in enumerate(lines):
        line = line[:-1]  # get rid of the newline character
        elves = line.split(",")
        start1, stop1 = elves[0].split("-")
        start2, stop2 = elves[1].split("-")
        # print(line, start1, stop1, start2, stop2)
        groups[i][0] = list(range(int(start1), int(stop1) + 1))
        groups[i][1] = list(range(int(start2), int(stop2) + 1))
        # print(groups[i])

reassignments = 0
for group in groups:
    overlapped = False
    shared = True
    for task in group[0]:
        if task not in group[1]:
            shared = False
    if shared:
        overlapped = True
    shared = True
    for task in group[1]:
        if task not in group[0]:
            shared = False
    if shared:
        overlapped = True
    if overlapped:
        # print(group)
        reassignments = reassignments + 1
print("Part 1:", reassignments)

# Part 2
overlapped = 0
for group in groups:
    overlap = False
    for task in group[0]:
        if task in group[1]:
            overlap = True
    if overlap:
        overlapped = overlapped + 1
print("Part 2:", overlapped)
