file1 = open('./5/input.txt', 'r')
lines = file1.readlines()
maxElements = 1000
matrix = []

for x in range(maxElements):
    temp = []
    for y in range(maxElements):
        temp.append(0)
    matrix.append(temp)

for line in lines:
    temp = line.replace('\n', '')
    pointsArr = temp.split(' -> ')
    points1 = pointsArr[0].split(',')
    points2 = pointsArr[1].split(',')

    if (points1[0] == points2[0]):
        if int(points1[1]) > int(points2[1]):
            for y in range(int(points2[1]), int(points1[1])+1):
                matrix[y][int(points1[0])] += 1
        else:
            for y in range(int(points1[1]), int(points2[1])+1):
                matrix[y][int(points1[0])] += 1
    elif (points1[1] == points2[1]):
        if int(points1[0]) > int(points2[0]):
            for x in range(int(points2[0]), int(points1[0])+1):
                matrix[int(points1[1])][x] += 1
        else:
            for x in range(int(points1[0]), int(points2[0])+1):
                matrix[int(points1[1])][x] += 1


    elif int(points1[1]) > int(points2[1]):
        y = range(int(points2[1]), int(points1[1])+1)[::-1]
        if int(points1[0]) >= int(points2[0]):
            for id, x in enumerate(range(int(points2[0]), int(points1[0])+1)[::-1]):
                matrix[y[id]][x] += 1
        else:
            for id, x in enumerate(range(int(points1[0]), int(points2[0])+1)):
                matrix[y[id]][x] += 1
    else:
        y = range(int(points1[1]), int(points2[1])+1)
        if int(points1[0]) >= int(points2[0]):
            for id, x in enumerate(range(int(points2[0]), int(points1[0])+1)[::-1]):
                matrix[y[id]][x] += 1
        else:
            for id, x in enumerate(range(int(points1[0]), int(points2[0])+1)):
                matrix[y[id]][x] += 1

count = 0
for y in matrix:
    for x in y:
        if x > 1:
            count += 1

print(count)