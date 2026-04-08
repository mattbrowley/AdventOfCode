with open("input2.txt", "r") as f:
    contents = f.readlines()

paper = 0
ribbon = 0
for i, line in enumerate(contents):
    firstx = 0
    secondx = 0
    for j, char in enumerate(line):
        if char == 'x':
            if firstx == 0:
                firstx = j
            else:
                secondx = j
    l = int(line[0:firstx])
    w = int(line[firstx+1:secondx])
    h = int(line[secondx+1:])
    
    s1 = l*w
    s2 = l*h
    s3 = w*h
    extra = min(s1, s2, s3)
    paper = paper + 2 * s1 + 2 * s2 + 2 * s3 + extra

    edges = [l, w, h]
    for i in range(len(edges)-1):
        for j in range(len(edges)-i-1):
            if edges[j]>edges[j+1]:
                edges[j], edges[j+1] = edges[j+1],edges[j]
    ribbon = ribbon + 2 * edges[0] + 2 * edges[1] + l * w * h
        

print("Paper required: {} sq ft".format(paper))
print("Ribbon required: {} ft".format(ribbon))

