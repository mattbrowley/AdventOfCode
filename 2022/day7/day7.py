import numpy as np

with open("day7data.txt", "r") as f:
    lines = f.readlines()

totalmem = 0


def findSize(index):
    global totalmem
    size = 0
    while True:
        if index == len(lines):
            print("last line completed")
            if size < 100001:
                totalmem = totalmem + size
                print(totalmem, size)
            return size, index
        words = lines[index].split(" ")
        index = index + 1
        if words[0] != "$" and words[0] != "dir":
            size = size + int(words[0])
        if words[1] == "cd":
            if words[2] == "..\n":
                print("directory complete:", size)
                if size < 100001:
                    totalmem = totalmem + size
                    print(totalmem, size)
                return size, index
            subsize, jump = findSize(index)
            size = size + subsize
            index = jump


completesize, jump = findSize(0)

print("Part 1:", totalmem)
print(completesize)
freemem = 70000000 - completesize
neededmem = 30000000 - freemem
print(neededmem)

smallest = 70000000


def findSmallest(index):
    global totalmem
    global smallest
    size = 0
    while True:
        if index == len(lines):
            print("last line completed")
            if size < 100001:
                totalmem = totalmem + size
                print(totalmem, size)
            return size, index
        words = lines[index].split(" ")
        index = index + 1
        if words[0] != "$" and words[0] != "dir":
            size = size + int(words[0])
        if words[1] == "cd":
            if words[2] == "..\n":
                print("directory complete:", size)
                if size >= neededmem and size < smallest:
                    smallest = size
                    print("New smallest:", smallest)
                if size < 100001:
                    totalmem = totalmem + size
                    print(totalmem, size)
                return size, index
            subsize, jump = findSmallest(index)
            size = size + subsize
            index = jump


filesize, jump = findSmallest(0)
print("Part 2:", smallest)
print(neededmem)
