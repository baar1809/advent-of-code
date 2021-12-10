def excludeChars(stringSave, excluded):
    for ex in excluded:
        for char in ex:
            stringSave = stringSave.replace(char, '')
    return stringSave

def check(inputNum, description):
    for id, desc in enumerate(description):
        for char in desc:
            if char not in inputNum:
                return { 'line': id, 'char': char}

file1 = open('./8/input.txt', 'r')
lines = [d.replace('\n', '') for d in file1.readlines()]

numbersArray = {
    '012456' : 0,
    '25' : 1,
    '02346' : 2,
    '02356' : 3,
    '1235' : 4,
    '01356' : 5,
    '013456' : 6,
    '025' : 7,
    '0123456' : 8,
    '012356' : 9,
}

adjacentLines = {
    2: 5,
    3: 1,
    4: 6
}

lenNum = [2, 4, 3, 7]
count = 0
finalResult = 0

for line in lines:
    numKeyCount = { 2: [], 3: [], 4: [], 5: [], 6: [], 7: [] }
    decryption = []
    nums = line.split(' | ')[0].split(' ')
    cypher = line.split(' | ')[1].split(' ')

    for i in range(7):
        decryption.append([])
    for num in nums:
        numKeyCount[len(num)].append(num)
    
    decryption[2] = decryption[5] = numKeyCount[2][0]
    decryption[0] = excludeChars(numKeyCount[3][0], [numKeyCount[2][0]])
    decryption[1] = decryption[3] = excludeChars(numKeyCount[4][0], [decryption[2], decryption[0]])
    decryption[6] = decryption[4] = excludeChars(numKeyCount[7][0], decryption)

    for six in numKeyCount[6]:
        missLine = check(six, decryption)
        if missLine['line'] == 1:
            missLine['line'] = 3
        decryption[missLine['line']] = missLine['char']
        decryption[adjacentLines[missLine['line']]] = excludeChars(decryption[adjacentLines[missLine['line']]], missLine['char'])
    
    result = ''

    for num in cypher:
        keys = []
        for char in num:
            for id, desc in enumerate(decryption):
                if char == desc:
                    keys.append(id)
        keys.sort()
        key = ''
        key = key.join([str(elem) for elem in keys])
        result += str(numbersArray[key])
    
    finalResult += int(result)

print(finalResult)






