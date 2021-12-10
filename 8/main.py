file1 = open('./8/input.txt', 'r')
lines = [d.replace('\n', '') for d in file1.readlines()]
lenNum = [2, 4, 3, 7]
count = 0

for line in lines:
    nums = line.split(' | ')[1].split(' ')
    for num in nums:
        if len(num) in lenNum:
            count += 1

print(count)