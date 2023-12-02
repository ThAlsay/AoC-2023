# Advent of Code 2023
# Solution of day 2 puzzle part 1
#
# Author Alonso Sayalero

def areGamesCorrect(games):
    correct = True
    for game in games:
        results = game.split(",")
        for result in results:
            result = result.split()
            match result[1]:
                case "red":
                    if int(result[0]) > 12:
                        correct = False
                case "green":
                    if int(result[0]) > 13:
                        correct = False
                case "blue":
                    if int(result[0]) > 14:
                        correct = False
    return correct

def main():
    try:
        file = open("./input.txt", "r").read().splitlines()
    except:
        print("Fail opening file")
        return
    
    totalSum = 0
    for line in file:
        gameId, games = line.split(':')
        games = games.split(';')

        print(gameId, games)
        if areGamesCorrect(games):
            totalSum += int(gameId.split()[1])

    print("The final result is: {}".format(totalSum))


if __name__ == "__main__":
    main()