file1 = open('./2/input.txt', 'r')
lines = file1.readlines()
newLines = []
for id in range(2, len(lines)):
    newLines.append(int(lines[id-2]) + int(lines[id-1]) + int(lines[id]))

count = 0
for id, line in enumerate(newLines):
    if (int(line) > int(newLines[id - 1])):
        print(int(line), int(newLines[id - 1]), id)
        count += 1
print(count)