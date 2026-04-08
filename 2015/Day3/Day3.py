with open("input3.txt", "r") as f:
    contents = f.read()

visited = [[0, 0]]
current_pos = [0, 0]
for i, char in enumerate(contents):
    if char == '<':
        current_pos[0] = current_pos[0]-1
    elif char == '>':
        current_pos[0] = current_pos[0]+1
    elif char == '^':
        current_pos[1] = current_pos[1]+1
    elif char == 'v':
        current_pos[1] = current_pos[1]-1
    visited.append([current_pos[0], current_pos[1]])

print("Total House Visits: {}".format(len(visited)))

culled = [[0, 0]]
for house in visited:
    unique = True
    for other in culled:
        if house == other:
            unique = False
    if unique:
        culled.append(house)

print("Total Unique Houses Visited: {}".format(len(culled)))

print("Part 2: Robo-Santa!")
# This time I will chech uniquness as I build the visited array

visited2 = [[0, 0]]
santa_pos = [0, 0]
robot_pos = [0, 0]
for i, char in enumerate(contents):
    unique = True
    if i % 2 == 0:
        if char == '<':
            santa_pos[0] = santa_pos[0]-1
        elif char == '>':
            santa_pos[0] = santa_pos[0]+1
        elif char == '^':
            santa_pos[1] = santa_pos[1]+1
        elif char == 'v':
            santa_pos[1] = santa_pos[1]-1
        for house in visited2:
            if house == santa_pos:
                unique = False
        if unique:
            visited2.append([santa_pos[0], santa_pos[1]])
    else:
        if char == '<':
            robot_pos[0] = robot_pos[0]-1
        elif char == '>':
            robot_pos[0] = robot_pos[0]+1
        elif char == '^':
            robot_pos[1] = robot_pos[1]+1
        elif char == 'v':
            robot_pos[1] = robot_pos[1]-1
        for house in visited2:
            if house == robot_pos:
                unique = False
        if unique:
            visited2.append([robot_pos[0], robot_pos[1]])

print("Total Unique Houses Visited: {}".format(len(visited2)))
