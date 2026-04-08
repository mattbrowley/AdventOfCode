import numpy as np

with open("input6.txt", "r") as f:
    lines = f.readlines()

def tokenize(line):
    command = "On"
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0
    spaces = []
    commas = []
    for i, char in enumerate(line):
        if char == ' ': spaces.append(i)
        if char == ',': commas.append(i)
    # print(spaces, spaces[0])
    # print(type(spaces), type(spaces[0]))

    if len(spaces)==3:
        command = "toggle"
        start_x = int(line[spaces[0]+1:commas[0]])
        start_y = int(line[commas[0]+1:spaces[1]])
        end_x = int(line[spaces[2]+1:commas[1]])
        end_y = int(line[commas[1]+1:])
    else:
        command = line[spaces[0]+1:spaces[1]]
        start_x = int(line[spaces[1]+1:commas[0]])
        start_y = int(line[commas[0]+1:spaces[2]])
        end_x = int(line[spaces[3]+1:commas[1]])
        end_y = int(line[commas[1]+1:])
    return command, start_x, start_y, end_x, end_y

lights = np.zeros([1000,1000])
for line in lines:
    command, start_x, start_y, end_x, end_y = tokenize(line)
    for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
            if command == "toggle":
                lights[x,y] = not lights[x,y]
            elif command == "on":
                lights[x,y] = 1
            elif command == "off":
                lights[x,y] = 0
print("Lights lit: {}".format(sum(sum(lights))))

lights = np.zeros([1000,1000])
for line in lines:
    command, start_x, start_y, end_x, end_y = tokenize(line)
    for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
            if command == "toggle":
                lights[x,y] = lights[x,y] + 2 
            elif command == "on":
                lights[x,y] = lights[x,y] + 1 
            elif command == "off":
                lights[x,y] = lights[x,y] - 1 
                if lights[x,y]<0:lights[x,y]=0
print("Total Brightness: {}".format(sum(sum(lights))))
