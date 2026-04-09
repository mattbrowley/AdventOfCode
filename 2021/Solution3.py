import numpy as np

with open("./Input3.txt", "r") as f:
    lines = f.readlines()
# Part 1

# Convert the data to a numpy array for easy slicing, etc.
data = np.zeros([len(lines), len(lines[0]) - 1])
for i, line in enumerate(lines):
    for j, bit in enumerate(line[:-1]):
        data[i, j] = int(bit)
gamma = 0
epsilon = 0
# Transpose the data to get columns instead of rows in the loop
for pow, bitcolumn in enumerate(data.T[::-1]):  # start with low bit
    if sum(bitcolumn) > len(bitcolumn) / 2:
        # 1 is more common
        gamma += 2**pow
    else:
        # 0 is more common
        epsilon += 2**pow
product = gamma * epsilon
print("Part 1")
print("======")
print(f"Gamma Rate: {bin(gamma)}  Epsilon Rate: {bin(epsilon)}")
print(f"Product: {product}")

# Part 2
OFilter = np.arange(0, len(lines), 1)
CFilter = np.arange(0, len(lines), 1)
# for i in range(11, -1, -1):
for i in range(12):
    OColumn = []
    for j in OFilter:
        OColumn.append(data[j][i])
    if sum(OColumn) >= len(OColumn) / 2:
        majority = 1
    else:
        majority = 0
    newO = []
    for j in OFilter:
        if data[j][i] == majority:
            newO.append(j)
    OFilter = newO
    if len(CFilter) > 1:
        CColumn = []
        for k in CFilter:
            CColumn.append(data[k][i])
        if sum(CColumn) >= len(CColumn) / 2:
            majority = 1
        else:
            majority = 0
        newC = []
        for k in CFilter:
            if data[k][i] != majority:
                newC.append(k)
        CFilter = newC
O2bin = data[OFilter[0]]
CO2bin = data[CFilter[0]]
O2 = 0
CO2 = 0
for i, (obit, cbit) in enumerate(zip(O2bin[::-1], CO2bin[::-1])):
    # print(obit, cbit)
    O2 += 2**i * obit
    CO2 += 2**i * cbit
print("Part 2")
print("======")
print(f"O2 Generator Rating: {O2}")
print(f"CO2 Generator Rating: {CO2}")
print(f"Product: {O2 * CO2}")
