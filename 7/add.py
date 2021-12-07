import numpy


file1 = open('./7/input.txt', 'r')
values = [int(d) for d in file1.readlines()[0].split(',')]
medianNum = int(numpy.around(numpy.mean(values)))
fuels = []

for median in range(medianNum-1, medianNum+1):
    fuels.append(0)
    for val in values:
        res = 0
        for ful in range(1, int(numpy.abs(val - median))+1):
            res += ful
        fuels[-1] += res

print(fuels, median, numpy.min(fuels))