import numpy as np

with open("day6data.txt", "r") as f:
    lines = f.readlines()
    stream = lines[0]

for i in range(len(stream)):
    unique = True
    if stream[i] in stream[i + 1 : i + 4]:
        unique = False
    if stream[i + 1] in stream[i + 2 : i + 4]:
        unique = False
    if stream[i + 2] == stream[i + 3]:
        unique = False
    if unique:
        print("Part 1:", i + 4)
        break

characters = 14
for i in range(len(stream)):
    unique = True
    for j in range(characters):
        if stream[i + j] in stream[i + j + 1 : i + characters]:
            unique = False
    if unique:
        print("Part 2:", i + characters)
        break
