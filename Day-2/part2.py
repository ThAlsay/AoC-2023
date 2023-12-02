# Advent of Code 2023
# Solution of day 2 puzzle part 2
#
# Author Alonso Sayalero

def minCubes(games: list[str]):
    minBlue = 1
    minRed = 1
    minGreen = 1

    for game in games:
        game = game.split(',')
        for cube in game:
            cube = cube.split()
            match cube[1]:
                case "red":
                    if int(cube[0]) > minRed:
                        minRed = int(cube[0])
                case "green":
                    if int(cube[0]) > minGreen:
                        minGreen = int(cube[0])
                case "blue":
                    if int(cube[0]) > minBlue:
                        minBlue = int(cube[0])

    return minRed, minBlue, minGreen


def main():
    try:
        file = open("./input.txt", "r").read().splitlines()
    except:
        print("Fail opening file")
        return
    
    totalSum = 0
    for line in file:
        games = line.split(':')[1].split(';')

        minRed, minBlue, minGreen = minCubes(games)

        totalSum += minRed * minBlue * minGreen



    print("The final result is: {}".format(totalSum))


if __name__ == "__main__":
    main()