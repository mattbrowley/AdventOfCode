with open("input5.txt", "r") as f:
    lines = f.readlines()

vowels = ['a', 'e', 'i', 'o', 'u']
forbidden = ["ab", "cd", "pq", "xy"]
nice = 0
for line in lines:
    num_vowels = 0
    double = False
    naughty = False
    for i, char in enumerate(line):
        for vowel in vowels:
            if char == vowel:
                num_vowels = num_vowels+1
        if i != 0:
            pair = line[i-1:i+1]
            if pair[0] == pair[1]:
                double = True
            for f_pair in forbidden:
                if pair == f_pair:
                    naughty = True
    if double and not naughty and num_vowels > 2:
        nice = nice+1
print("Number of nice lines: {}".format(nice))
print("Part 2 - New Rules!")

nice = 0
for line in lines:
    split = False
    repeat = False
    for i, char in enumerate(line):
        if i < len(line)-2:
            if char == line[i+2]:
                split = True
            if i != 0:
                pair = line[i-1:i+1]
                for j in range(i+1, len(line)-1):
                    others = line[j:j+2]
                    if pair == others:
                        repeat = True
    if split and repeat:
        nice = nice+1
print("Number of nice lines: {}".format(nice))
