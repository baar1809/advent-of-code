file1 = open('./3/input.txt', 'r')
lines = file1.readlines()
len = 12
counts = []

for id in range(0, len):
    counts.append([0, 0])

for line in lines:
    temp = line.replace('\n', '')
    for id, bite in enumerate(temp):
        counts[id][int(bite)] += 1

gammaRate = ''
epsilonRate = ''

for count in counts:
    gammaRate += str(count.index(max(count)))
    epsilonRate += str(count.index(min(count)))

print(int(gammaRate, 2) * int(epsilonRate, 2))