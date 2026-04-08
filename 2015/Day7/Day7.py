import numpy as np

with open("input7.txt", "r") as f:
    lines = f.readlines()


def str_to_index(string):
    if len(string) == 1:
        index = ord(string[0])-97
    else:
        index = (ord(string[0])-96)*26+ord(string[1])-97
    return index


def bit_not(n, numbits=8):
    return (1 << numbits) - 1 - n


def tokenize(line):
    command = None
    in1 = None
    in2 = None
    target = None
    spaces = []
    for i, char in enumerate(line):
        if char == ' ':
            spaces.append(i)
    if len(spaces) == 2:
        command = "STORE"
        in1 = line[:spaces[0]]
        target = line[spaces[1]+1:]
        # print(line)
        # print(in1, target)
    elif len(spaces) == 3:
        command = "NOT"
        in1 = line[spaces[0]+1:spaces[1]]
        target = line[spaces[2]+1:]
        # print(line)
        # print(in1, target)
    else:
        command = line[spaces[0]+1:spaces[1]]
        in1 = line[:spaces[0]]
        in2 = line[spaces[1]+1:spaces[2]]
        target = line[spaces[3]+1:]
        # print(line)
        # print(in1, command, in2, target)

    return command, in1, in2, target[:-1]


# This is not pretty. The strategy is to iterate over the lines and detect which
# commands cannot be completed because one or more of its inputs are not yet
# resolved. If a line is completed, then it is removed. After all the lines have
# been analyzed, we go through them again quasi-recursively until they have all
# been successfully excecuted
outputs = [-1]*len(lines)


circuit = []
for i, line in enumerate(lines):
    command, in1, in2, target = tokenize(line)
    if command == "OR" or command == "AND":
        if in1 == '1':
            circuit.append([command, -1, str_to_index(in2), str_to_index(target)])
        else:
            circuit.append([command, str_to_index(in1), str_to_index(in2), str_to_index(target)])
    elif command == "NOT":
        circuit.append([command, str_to_index(in1), str_to_index(target)])
    elif command == "STORE":
        try:
            value = int(in1)
            print("Stored value of: {}".format(value))
            outputs[str_to_index(target)] = value
        except:
            circuit.append([command, str_to_index(in1), str_to_index(target)])
            print("Remember command to store from {} to {}".format(in1, target))
    elif command == "RSHIFT" or command == "LSHIFT":
        circuit.append([command, str_to_index(in1), int(in2), str_to_index(target)])
    else:
        print("Failed to parse line: {}".format(line))

while outputs[0] == -1:
# i = 0
# while i < 18:
#     print(i)
#     i += 1
#     print(outputs)
    for line in circuit:
        command = line[0]
        if command == "OR":
            in1 = line[1]
            in2 = line[2]
            if outputs[in1] > -1 and outputs[in2] > -1:
                target = line[3]
                output = outputs[in1] | outputs[in2]
                if outputs[target] == -1:
                    print(line, output)
                    print(outputs[in1], outputs[in2], output)
                    print(bin(outputs[in1]))
                    print(bin(outputs[in2]))
                    print(bin(output))
                    outputs[target] = output
        elif command == "AND":
            in1 = line[1]
            in2 = line[2]
            if in1 == -1 and outputs[in2] > -1:
                target = line[3]
                output = 1 & outputs[in2]
                if outputs[target] == -1:
                    print(line, output)
                    print(1, outputs[in2], output)
                    print(bin(1))
                    print(bin(outputs[in2]))
                    print(bin(output))
                    outputs[target] = output
            elif outputs[in1] > -1 and outputs[in2] > -1:
                target = line[3]
                output = outputs[in1] & outputs[in2]
                if outputs[target] == -1:
                    print(line, output)
                    print(outputs[in1], outputs[in2], output)
                    print(bin(outputs[in1]))
                    print(bin(outputs[in2]))
                    print(bin(output))
                    outputs[target] = output
        elif command == "STORE":
            in1 = line[1]
            if outputs[in1] > -1:
                target = line[2]
                output = outputs[in1]
                if outputs[target] == -1:
                    print(line, output)
                    print(outputs[in1], output)
                    print(bin(outputs[in1]))
                    print(bin(output))
                    outputs[target] = outputs[in1]
        elif command == "NOT":
            in1 = line[1]
            if outputs[in1] > -1:
                target = line[2]
                output = bit_not(outputs[in1], 16)
                if outputs[target] == -1:
                    print(line, output)
                    print(outputs[in1], output)
                    print(bin(outputs[in1]))
                    print(bin(output))
                    outputs[target] = output
        elif command == "RSHIFT":
            in1 = line[1]
            in2 = line[2]
            if outputs[in1] > -1:
                target = line[3]
                output = outputs[in1] >> int(in2)
                if outputs[target] == -1:
                    print(line, output)
                    print(outputs[in1], output)
                    print(bin(outputs[in1]))
                    print(bin(output))
                    outputs[target] = output
        elif command == "LSHIFT":
            in1 = line[1]
            in2 = line[2]
            if outputs[in1] > -1:
                target = line[3]
                output = (outputs[in1] << int(in2)) % 2**16
                if outputs[target] == -1:
                    print("{}=={}".format(outputs[target], -1))
                    print(line, output)
                    print(outputs[in1], outputs[in1] << int(in2))
                    print(bin(outputs[in1]))
                    print(bin(outputs[in1] << int(in2)))
                    outputs[target] = output
        else:
            print("Unable to parse line: {}".format(line))
    completed = 0
    for output in outputs:
        if output > -1:
            completed += 1
    print("Completed: {} of {}".format(completed, len(circuit)))
    print("lx ({}):{}".format(str_to_index('lx'), outputs[str_to_index('lx')]))
print(outputs)
print("a:{}".format(outputs[0]))
print("lx ({}):{}".format(str_to_index('lx'), outputs[str_to_index('lx')]))

first_a = outputs[0]

outputs = [-1]*len(lines)

circuit = []
for i, line in enumerate(lines):
    command, in1, in2, target = tokenize(line)
    if command == "OR" or command == "AND":
        if in1 == '1':
            circuit.append([command, -1, str_to_index(in2), str_to_index(target)])
        else:
            circuit.append([command, str_to_index(in1), str_to_index(in2), str_to_index(target)])
    elif command == "NOT":
        circuit.append([command, str_to_index(in1), str_to_index(target)])
    elif command == "STORE":
        try:
            value = int(in1)
            print("Stored value of: {}".format(value))
            outputs[str_to_index(target)] = value
        except:
            circuit.append([command, str_to_index(in1), str_to_index(target)])
            print("Remember command to store from {} to {}".format(in1, target))
    elif command == "RSHIFT" or command == "LSHIFT":
        circuit.append([command, str_to_index(in1), int(in2), str_to_index(target)])
    else:
        print("Failed to parse line: {}".format(line))

outputs[1] = first_a

while outputs[0] == -1:
# i = 0
# while i < 18:
#     print(i)
#     i += 1
#     print(outputs)
    for line in circuit:
        command = line[0]
        if command == "OR":
            in1 = line[1]
            in2 = line[2]
            if outputs[in1] > -1 and outputs[in2] > -1:
                target = line[3]
                output = outputs[in1] | outputs[in2]
                if outputs[target] == -1:
                    print(line, output)
                    print(outputs[in1], outputs[in2], output)
                    print(bin(outputs[in1]))
                    print(bin(outputs[in2]))
                    print(bin(output))
                    outputs[target] = output
        elif command == "AND":
            in1 = line[1]
            in2 = line[2]
            if in1 == -1 and outputs[in2] > -1:
                target = line[3]
                output = 1 & outputs[in2]
                if outputs[target] == -1:
                    print(line, output)
                    print(1, outputs[in2], output)
                    print(bin(1))
                    print(bin(outputs[in2]))
                    print(bin(output))
                    outputs[target] = output
            elif outputs[in1] > -1 and outputs[in2] > -1:
                target = line[3]
                output = outputs[in1] & outputs[in2]
                if outputs[target] == -1:
                    print(line, output)
                    print(outputs[in1], outputs[in2], output)
                    print(bin(outputs[in1]))
                    print(bin(outputs[in2]))
                    print(bin(output))
                    outputs[target] = output
        elif command == "STORE":
            in1 = line[1]
            if outputs[in1] > -1:
                target = line[2]
                output = outputs[in1]
                if outputs[target] == -1:
                    print(line, output)
                    print(outputs[in1], output)
                    print(bin(outputs[in1]))
                    print(bin(output))
                    outputs[target] = outputs[in1]
        elif command == "NOT":
            in1 = line[1]
            if outputs[in1] > -1:
                target = line[2]
                output = bit_not(outputs[in1], 16)
                if outputs[target] == -1:
                    print(line, output)
                    print(outputs[in1], output)
                    print(bin(outputs[in1]))
                    print(bin(output))
                    outputs[target] = output
        elif command == "RSHIFT":
            in1 = line[1]
            in2 = line[2]
            if outputs[in1] > -1:
                target = line[3]
                output = outputs[in1] >> int(in2)
                if outputs[target] == -1:
                    print(line, output)
                    print(outputs[in1], output)
                    print(bin(outputs[in1]))
                    print(bin(output))
                    outputs[target] = output
        elif command == "LSHIFT":
            in1 = line[1]
            in2 = line[2]
            if outputs[in1] > -1:
                target = line[3]
                output = (outputs[in1] << int(in2)) % 2**16
                if outputs[target] == -1:
                    print("{}=={}".format(outputs[target], -1))
                    print(line, output)
                    print(outputs[in1], outputs[in1] << int(in2))
                    print(bin(outputs[in1]))
                    print(bin(outputs[in1] << int(in2)))
                    outputs[target] = output
        else:
            print("Unable to parse line: {}".format(line))
    completed = 0
    for output in outputs:
        if output > -1:
            completed += 1
    print("Completed: {} of {}".format(completed, len(circuit)))
    print("lx ({}):{}".format(str_to_index('lx'), outputs[str_to_index('lx')]))
print(outputs)
print("a:{}".format(outputs[0]))
print("lx ({}):{}".format(str_to_index('lx'), outputs[str_to_index('lx')]))
