import hashlib

key = "bgvyzdsv"
solved = False
suffix = 1
while not solved:
    test = key + str(suffix)
    hashdigest = hashlib.md5(test.encode()).hexdigest()
    zeros = True
    for char in hashdigest[:5]:
        if char != '0':
            zeros = False
    if zeros:
        solved = True
    else:
        suffix = suffix + 1
print("Hash: {}".format(hashdigest))
print("Solution: {}".format(test))
print("Part 2 - six zeros!")
solved = False
suffix = 1
while not solved:
    test = key + str(suffix)
    hashdigest = hashlib.md5(test.encode()).hexdigest()
    zeros = True
    for char in hashdigest[:6]:
        if char != '0':
            zeros = False
    if zeros:
        solved = True
    else:
        suffix = suffix + 1
print("Hash: {}".format(hashdigest))
print("Solution: {}".format(test))

