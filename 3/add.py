file1 = open('./3/input.txt', 'r')
lines = file1.readlines()
leng = 12
counts = []

def sanitize(item):
    return item.replace('\n', '')

def getOxygen(lines, pos, counts):
    if (len(lines) == 1):
        return lines[0]

    tepmLines = []

    for line in lines:
        if (counts[pos][0] == counts[pos][1]):
            if (int(line[pos]) == 1):
                tepmLines.append(line)
        else:
            if (int(line[pos]) == int(counts[pos].index(max(counts[pos])))):
                tepmLines.append(line)

    if (pos != leng - 1):
        pos += 1
        counts[pos] = [0, 0]
        for tempLine in tepmLines:
            counts[pos][int(tempLine[pos])] += 1

    return getOxygen(tepmLines, pos, counts)

def getCO2(lines, pos, counts):
    if (len(lines) == 1):
        return lines[0]

    tepmLines = []

    for line in lines:
        if (counts[pos][0] == counts[pos][1]):
            if (int(line[pos]) == 0):
                tepmLines.append(line)
        else:
            if (int(line[pos]) == int(counts[pos].index(min(counts[pos])))):
                tepmLines.append(line)

    if (pos != leng - 1):
        pos += 1
        counts[pos] = [0, 0]
        for tempLine in tepmLines:
            counts[pos][int(tempLine[pos])] += 1
    
    return getCO2(tepmLines, pos, counts)

lines = list(map(sanitize, lines))

for id in range(0, leng):
    counts.append([0, 0])

for line in lines:
    for id, bite in enumerate(line):
        counts[id][int(bite)] += 1

ox = getOxygen(lines, 0, counts)
co = getCO2(lines, 0, counts)

print(int(ox, 2) * int(co, 2))
