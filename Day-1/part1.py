# Advent of Code 2023
# Solution of day 1 puzzle part 1
#
# Author Alonso Sayalero

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

        print("{}, {}".format(mostLeft, mostRight))
        totalSum += mostLeft * 10 + mostRight
    
    print("The final value is: {}".format(totalSum))

if __name__ == "__main__":
    main()