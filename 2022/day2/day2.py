import numpy as np

decoder = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

with open("day2data.txt", "r") as f:
    lines = f.readlines()
    numRounds = len(lines)
    rounds = np.empty([numRounds, 2])
    for i, line in enumerate(lines):
        rounds[i][0] = decoder[line[0]]
        rounds[i][1] = decoder[line[2]]

score = 0
for round in rounds:
    score = score + round[1]
    outcome = (round[1] - round[0]) % 3
    if outcome == 0:
        score = score + 3
    elif outcome == 1:
        score = score + 6
print("Part 1 Score:", score)

# Part Two
score = 0
for round in rounds:
    if round[1] == 1:
        if round[0] == 1:
            score = score + 3
        else:
            score = score + round[0] - 1
    elif round[1] == 2:
        score = score + 3 + round[0]
    elif round[1] == 3:
        score = score + 6 + (round[0] % 3 + 1)

print("Part 2 Score:", score)
