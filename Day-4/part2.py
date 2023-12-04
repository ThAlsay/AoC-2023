# Advent of Code 2023
# Solution of day 4 puzzle part 2
#
# Author Alonso Sayalero

from xml.etree.ElementPath import find


def findWinners(winArray, chosenArray):
    winArray = set(winArray)
    number = 0
    for num in chosenArray:
        if num in winArray:
            number += 1
    return number

def main():
    try:
        file = open("./input.txt", "r").read().splitlines()
    except:
        print("Fail opening file.\n")
        return
    
    totalSum = 0
    counter = 0
    numberCopies = [1 for i in range(0, len(file))]
    for line in file:
        winNumbers, chosenNumbers = line.split(':')[1].split('|')
        winNumbers = winNumbers.split()
        chosenNumbers = chosenNumbers.split()
        winNumbers = [int(winNumbers[i]) for i in range(0, len(winNumbers))]
        chosenNumbers = [int(chosenNumbers[i]) for i in range(0, len(chosenNumbers))]

        numberWinners = findWinners(winNumbers, chosenNumbers)
        for i in range(1, numberWinners + 1):
            numberCopies[counter + i] = numberCopies[counter + i] + 1 * numberCopies[counter]
        counter += 1
    totalSum = sum(numberCopies)

    print("The final value is: {}".format(totalSum))

if __name__ == "__main__":
    main()