import numpy as np

with open("day3data.txt", "r") as f:
    lines = f.readlines()
    numPacks = len(lines)
    packs = np.empty([numPacks, 2], dtype=object)
    for i, line in enumerate(lines):
        line = line[:-1]  # get rid of the newline character
        quantity = int(len(line) / 2)
        packs[i][0] = line[0:quantity]
        packs[i][1] = line[quantity:]

priority = 0
for pack in packs:
    for char in pack[0]:
        if char in pack[1]:
            priority = priority + ord(char) - 38 - ord(char) // 95 * 58
            break

print("Part 1:", priority)

# Part 2
priority = 0
combined = np.empty(len(packs), dtype=object)
for i in range(len(packs)):
    combined[i] = packs[i][0] + packs[i][1]

for i in range(len(combined) // 3):
    for char in combined[i * 3]:
        print(char)
        if char in combined[i * 3 + 1] and char in combined[i * 3 + 2]:
            priority = priority + ord(char) - 38 - ord(char) // 95 * 58
            break


print("Part 2:", priority)
