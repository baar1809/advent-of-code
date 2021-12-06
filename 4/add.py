class Card:
    def __init__(self) -> None:
        self.lines = []
        self.countLinesInCard = 5
        self.haveWinners = False
        self.columns = []
        for i in range(self.countLinesInCard):
            self.columns.append(Column())

    def addLine(self, line):
        self.lines.append(line)
        for id, num in enumerate(line.getNumbers()):
            self.columns[id].addNumber(num)


    def isFull(self):
        return len(self.lines) >= self.countLinesInCard

    def isWinner(self):
        for line in self.lines:
            if line.isWinner():
                return True
        for column in self.columns:
            if column.isWinner():
                return True

        return False

    def setWinnerFlag(self):
        self.haveWinners = True

    def checkNumber(self, number):
        for line in self.lines:
            line.checkNumber(number)
        for column in self.columns:
            column.checkNumber(number)

    def getWinnerLine(self):
         for line in self.lines:
            if line.isWinner():
                return line

    def getSumOfNonMarcirateNumber(self):
        temp = []
        for line in self.lines:
            temp = temp + line.getNonMarcirateNumber()
        return sum(map(int, temp))


class Line:
    def __init__(self) -> None:
        self.marcirateNum = []
        self.numbers = []

    def setNumbers(self, numbersString):
        if (numbersString[0] == ' '):
            numbersString = numbersString[1:]
        self.numbers = numbersString.replace('  ', ' ').split(' ')

    def checkNumber(self, number):
        if (number in self.numbers):
            self.marcirateNum.append(number)

    def isWinner(self):
        return len(self.marcirateNum) >= len(self.numbers)

    def getNumbers(self):
        return self.numbers

    def getNonMarcirateNumber(self):
        return list(set(self.numbers) - set(self.marcirateNum))

class Column:
    def __init__(self) -> None:
        self.marcirateNum = []
        self.numbers = []

    def addNumber(self, numberString):
        self.numbers.append(numberString)

    def checkNumber(self, number):
        if (number in self.numbers):
            self.marcirateNum.append(number)

    def isWinner(self):
        return len(self.marcirateNum) >= len(self.numbers)
        

file1 = open('./4/input.txt', 'r')
lines = file1.readlines()
count = 1
cards = [Card()]
winNumbers = lines[0].replace('\n', '').split(',')

for line in lines:
    temp = line.replace('\n', '')
    if temp != '' and count != 1:
        line = Line()
        line.setNumbers(temp)
        if (cards[-1].isFull()):
            cards.append(Card())
        cards[-1].addLine(line)
    count += 1

winners = []
lastNum = 0
winner = False

for winNum in winNumbers:
    for card in cards:
        card.checkNumber(winNum)
        if card.isWinner():
            if not card.haveWinners:
                winners.append(card)
            card.setWinnerFlag()
            if len(winners) == len(cards):
                winner = card
                lastNum = winNum
                break
    if winner:
        break

print(123, winner.getSumOfNonMarcirateNumber(), lastNum, winner.getSumOfNonMarcirateNumber() * int(lastNum))