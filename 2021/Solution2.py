with open("Input2.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    print(line)
# Part 1
xpos = 0
zpos = 0
for line in lines:
    dir, dist = line.split()
    if dir == "forward":
        xpos += int(dist)
    elif dir == "up":
        zpos -= int(dist)
    elif dir == "down":
        zpos += int(dist)
print("Part 1")
print("======")
print(f"X-travel: {xpos}  Z-travel: {zpos}")
print(f"Product: {xpos * zpos}")

# Part 2
xpos = 0
zpos = 0
aim = 0
for line in lines:
    dir, dist = line.split()
    if dir == "forward":
        xpos += int(dist)
        zpos += aim * int(dist)
    elif dir == "up":
        aim -= int(dist)
    elif dir == "down":
        aim += int(dist)
print("Part 2")
print("======")
print(f"X-travel: {xpos}  Z-travel: {zpos}")
print(f"Product: {xpos * zpos}")
