# Advent of Code 2023
# Solution of day 3 puzzle part 1
#
# Author Alonso Sayalero

def numberLength(line: str):
    finalNumber = int(line[0])
    length = 0
    for i in range(1, len(line)):
        if not line[i].isdigit():
            return finalNumber, length
        else:
            finalNumber = finalNumber * 10 + int(line[i])
            length += 1
    return finalNumber, length

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
        if i != 0:
            previousLine = file[i - 1]
        if i != len(file) - 1:
            nextLine = file[i + 1]

        j = 0
        print(len(currentLine))
        while j < len(currentLine):
            if currentLine[j].isdigit():
                isValid = False 
                sumDigit, length = numberLength(currentLine[slice(j, len(currentLine))])
                print(sumDigit, length)
                for k in range(j, j + length + 1):
                    if i != 0:
                        if previousLine[k] != '.' and not previousLine[k].isdigit():
                            print("First",sumDigit)
                            isValid = True
                        if j != 0: 
                            if (previousLine[k - 1] != '.' and not previousLine[k -1].isdigit() \
                            or currentLine[k - 1] != '.' and not currentLine[k - 1].isdigit()):
                                print("Third",sumDigit)
                                isValid = True
                        if k < len(currentLine) - 1:
                            if (previousLine[k + 1] != '.' and not previousLine[k + 1].isdigit() \
                            or currentLine[k + 1] != '.' and not currentLine[k + 1].isdigit()):
                                print("Fourth",sumDigit)
                                isValid = True
                    if i != len(file) - 1:
                        if nextLine[k] != '.' and not nextLine[k].isdigit():
                            print("Second",sumDigit)
                            isValid = True
                        if j != 0: 
                            if (nextLine[k - 1] != '.' and not nextLine[k - 1].isdigit() \
                            or currentLine[k - 1] != '.' and not currentLine[k - 1].isdigit()):
                                print("Fifth",sumDigit)
                                isValid = True
                        if k < len(currentLine) - 1: 
                            if (nextLine[k + 1] != '.' and not nextLine[k + 1].isdigit() \
                            or currentLine[k + 1] != '.' and not currentLine[k + 1].isdigit()):
                                print("Sixth",sumDigit)
                                isValid = True
                if isValid:
                    totalSum += sumDigit
                j += length
            j += 1

    print("The final value is {}".format(totalSum))
    
if __name__ == "__main__":
    main()