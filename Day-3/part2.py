# Advent of Code 2023
# Solution of day 3 puzzle part 2
#
# Author Alonso Sayalero

def getLeft(line, start):
    number = 0
    i = start - 1
    while i >= 0:
        if not line[i].isdigit():
            break
        number = number + int(line[i]) * 10 ** (start - i - 1)
        i -= 1
    return number

def getRight(line, start):
    number = 0
    i = start + 1
    while i < len(line):
        if not line[i].isdigit():
            break
        number = number * 10 + int(line[i])
        i += 1
    return number

def getCenter(line, start):
    number = int(line[start])
    if start != 0 and line[start - 1].isdigit():
        i = start - 1
        while i >= 0:
            if not line[i].isdigit():
                break
            number = number + int(line[i]) * 10 ** (start - i)
            i -= 1
    if start != len(line) - 1 and line[start + 1].isdigit():
        i = start + 1
        while i < len(line):
            if not line[i].isdigit():
                break
            number = number * 10 + int(line[i])
            i += 1
    return number

def main():
    try:
        file = open("./input.txt", "r").read().splitlines()
    except:
        print("Fail opening file")
        return
    
    totalSum = 0
    for i in range(0, len(file)):
        currentLine = file[i]
        previousLine = []
        nextLine = []
        canUp = False
        canDown = False
        if i != 0:
            previousLine = file[i - 1]
            canUp = True
        if i != len(file) - 1:
            nextLine = file[i + 1]
            canDown = True
        
        for j in range(0, len(currentLine)):
            if currentLine[j] == '*':
                upCenter = 0
                upLeft = 0
                upRight = 0
                left = 0
                right = 0
                downCenter = 0
                downLeft = 0
                downRight = 0

                if j != 0:
                    if currentLine[j - 1].isdigit():
                        left = 1
                    if canUp:
                        if previousLine[j].isdigit():
                            upCenter = 1
                        elif previousLine[j - 1].isdigit():
                            upLeft = 1
                    if canDown:
                        if nextLine[j].isdigit():
                            downCenter = 1
                        elif nextLine[j - 1].isdigit():
                            downLeft = 1
                if j != len(currentLine) - 1:
                    if currentLine[j + 1].isdigit():
                        right = 1
                    if canUp:
                        if previousLine[j].isdigit():
                            upCenter = 1
                        elif previousLine[j + 1].isdigit():
                            upRight = 1
                    if canDown:
                        if nextLine[j].isdigit():
                            downCenter = 1
                        elif nextLine[j + 1].isdigit():
                            downRight = 1
                if upCenter + upLeft + upRight + left + right + downCenter + downLeft + downRight == 2:
                    auxNum = 1
                    if upCenter == 1:
                        auxNum *= getCenter(previousLine, j)
                    else:
                        if upLeft == 1:
                            auxNum *= getLeft(previousLine, j)
                        if upRight == 1:
                            auxNum *= getRight(previousLine, j)
                    if downCenter == 1:
                        auxNum *= getCenter(nextLine, j)
                    else:
                        if downLeft == 1:
                            auxNum *= getLeft(nextLine, j)
                        if downRight == 1:
                            auxNum *= getRight(nextLine, j)
                    if left == 1:
                        auxNum *= getLeft(currentLine, j)
                    if right == 1:
                        auxNum *= getRight(currentLine, j)
                    totalSum += auxNum

    print("The final value is {}".format(totalSum))
    
if __name__ == "__main__":
    main()