import numpy as np

with open("day5data.txt", "r") as f:
    lines = f.readlines()
    numInstructions = len(lines[10:])
    instructions = np.empty([numInstructions, 3], dtype=int)
    for i, line in enumerate(lines[10:]):
        words = line.split(" ")
        instructions[i][0] = int(words[1])
        instructions[i][1] = int(words[3]) - 1
        instructions[i][2] = int(words[5]) - 1

stacks = [
    "HBVWNMLP",
    "MQH",
    "NDBGFQML",
    "ZTFQMWG",
    "MTHP",
    "CBMJDHGT",
    "MNBFVR",
    "PLHMRGS",
    "PDBCN",
]


def move(quantity, source, target):
    for i in range(quantity):
        stacks[target] = stacks[target] + stacks[source][-1]
        stacks[source] = stacks[source][:-1]


for quantity, source, target in instructions:
    move(quantity, source, target)

print("Part 1")
for stack in stacks:
    print(stack[-1])

# Part 2
stacks = [
    "HBVWNMLP",
    "MQH",
    "NDBGFQML",
    "ZTFQMWG",
    "MTHP",
    "CBMJDHGT",
    "MNBFVR",
    "PLHMRGS",
    "PDBCN",
]


def move2(quantity, source, target):
    stacks[target] = stacks[target] + stacks[source][-quantity:]
    stacks[source] = stacks[source][:-quantity]


for quantity, source, target in instructions:
    move2(quantity, source, target)

print("Part 2")
for stack in stacks:
    print(stack[-1])
