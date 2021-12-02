file1 = open('./1/input.txt', 'r')
lines = file1.readlines()
count = 0
for id, line in enumerate(lines):
    if (id > 0):
        if (int(line) > int(lines[id - 1])):
            count += 1
print(count)