# Advent of Code 2023
# Solution of day 4 puzzle part 1
#
# Author Alonso Sayalero

def findNumbers(winArray, chosenArray):
    winArray = set(winArray)
    number = 0
    for num in chosenArray:
        if num in winArray:
            if number == 0:
                number = 1
            else:
                number *= 2
    return number

def main():
    try:
        file = open("./input.txt", "r").read().splitlines()
    except:
        print("Fail opening file.\n")
        return
    
    totalSum:int = 0
    for line in file:
        winNumbers, chosenNumbers = line.split(':')[1].split('|')
        winNumbers = winNumbers.split()
        chosenNumbers = chosenNumbers.split()
        winNumbers = [int(winNumbers[i]) for i in range(0, len(winNumbers))]
        chosenNumbers = [int(chosenNumbers[i]) for i in range(0, len(chosenNumbers))]

        totalSum += findNumbers(winNumbers, chosenNumbers)
        
    print("The final value is: {}".format(totalSum))

if __name__ == "__main__":
    main()