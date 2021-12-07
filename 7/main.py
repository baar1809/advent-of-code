import numpy


file1 = open('./7/input.txt', 'r')
values = [int(d) for d in file1.readlines()[0].split(',')]
median = numpy.median(values)
fuel = 0

for val in values:
    fuel += int(numpy.abs(val - median))

print(fuel)