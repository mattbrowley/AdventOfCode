# Part 1
with open("Input1.txt", "r") as f:
    lines = f.readlines()

depths = []
for line in lines:
    depths.append(int(line))
count = 0
previous = 999999999

for depth in depths:
    if depth > previous:
        count += 1
    previous = depth
print(f"Solution to part 1: {count}")

# Part 2
count = 0
previous = 999999999
for index in range(len(depths) - 2):
    depth = depths[index] + depths[index + 1] + depths[index + 2]
    if depth > previous:
        count += 1
    previous = depth
print(f"Solution to part 2: {count}")
