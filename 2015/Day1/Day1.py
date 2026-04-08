with open("input1.txt", "r") as f:
    contents = f.read()

left = 0
right = 0
floor = 0
for i, char in enumerate(contents):
    if char == '(':
        left = left+1
        floor = floor+1
    if char == ')':
        right = right+1
        floor = floor-1
    if floor == -1:
        print("first descent into the basement on instruction #{}".format(i+1))

print("left: {}".format(left))
print("right: {}".format(right))
print("final floor: {}".format(floor))
