from collections import Counter

file1 = open('./6/input.txt', 'r')
ages = [int(d) for d in file1.readlines()[0].split(',')]

lifes = dict(Counter(ages))
days = 256
for day in range(1, days+1):
    lifes = {l: (0 if lifes.get(l+1) is None else lifes.get(l+1)) for l in range(-1, 8)}
    lifes[8] = lifes[-1]
    lifes[6] += lifes[-1]
    lifes[-1] = 0

print(sum(lifes.values()))