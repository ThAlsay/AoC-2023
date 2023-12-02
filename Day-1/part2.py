# Advent of Code 2023
# Solution of day 1 puzzle part 2
#
# Author Alonso Sayalero

numbersDict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def findFirstDigit(line, start):
    for i in range(start, len(line)):
        if line[i].isdigit():
            return i
        
    return len(line)

def findLowestString(line):
    lastPosition = -1
    number = -1
    for key in numbersDict:
        position = line.find(key)
        if key in line and (lastPosition == -1 or lastPosition > position):
            number = numbersDict[key]
            lastPosition = position

    return number
        

def main():
    try:
        file = open("./input.txt", "r").read().splitlines()
    except:
        print("Fail opening file.\n")
        return
    
    totalSum = 0
    for line in file:
        print(line)
        mostLeft: int = -1
        mostRight: int = -1

        for i in range(0, len(line)):
            if line[i].isdigit() and mostLeft == -1:
                mostLeft = int(line[i])
                mostRight = int(line[i])
            elif line[i].isdigit():
                mostRight = int(line[i])
            else:
                number = findLowestString(line[slice(i, findFirstDigit(line, i))])
                if mostLeft == -1 and number != -1:
                    mostLeft = number
                    mostRight = number
                elif number != -1:
                    mostRight = number

        print("{}, {}".format(mostLeft, mostRight))
        totalSum += mostLeft * 10 + mostRight
    
    print("The final value is: {}".format(totalSum))

if __name__ == "__main__":
    main()