class Lanternfish:
    def __init__(self, age) -> None:
        self.age = int(age)

    def checkAge(self) -> bool:
        if (self.age == 0):
            self.setAge(6)
            return True
        self.age -= 1
        return False
    
    def setAge(self, age):
        self.age = age



file1 = open('./6/input.txt', 'r')
ages = file1.readlines()[0].split(',')
lanternfishes = []
daysCount = 256

for age in ages:
    lanternfishes.append(Lanternfish(age))

fishesCount = len(lanternfishes)
for day in range(daysCount+1):
    fishesCount = len(lanternfishes)
    for fishId in range(fishesCount):
        if lanternfishes[fishId].checkAge():
            lanternfishes.append(Lanternfish(8))
    print(day, fishesCount)