# Advent of Code 2023
# Solution of day 7 puzzle part 2
#
# Author Alonso Sayalero
import functools

def sortComparator(first, second):
    if first[2] > second[2]:
        return 1
    elif first[2] < second[2]:
        return -1
    else:
        order = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
        for i in range(5):
            if not first[0][i].isdigit():
                cmpA = order[first[0][i]]
            else:
                cmpA = int(first[0][i])
            if not second[0][i].isdigit():
                cmpB = order[second[0][i]]
            else:
                cmpB= int(second[0][i])

            if cmpA > cmpB:
                return 1
            elif cmpA < cmpB:
                return -1
        else:
            return 0

def getForce(hand: str):
    allCards = {}
    for card in hand:
        if card in allCards:
            allCards[card] += 1
        else:
            allCards[card] = 1
    if "J" in allCards:
        newValue = 0
        newKey = ""
        for key in allCards:
            if key != "J" and allCards[key] > newValue:
                newValue = allCards[key]
                newKey = key
        if newKey != "":
            allCards[newKey] += allCards["J"]
            del allCards["J"]

    key = list(allCards)[0]
    if len(allCards) == 1:
        return 6
    elif len(allCards) == 2:
        if allCards[key] == 4 or allCards[key] == 1:
            return 5
        else:
            return 4
    elif len(allCards) == 3:
        if allCards[key] == 3:
            return 3
        elif allCards[key] == 1:
            key = list(allCards)[1]
            if allCards[key] == 3 or allCards[key] == 1:
                return 3
            else:
                return 2
        else:
            return 2
    elif len(allCards) == 4:
        return 1
    else:
        return 0

def main():
    try:
        file = open("./input.txt", "r").read().splitlines()
    except:
        print("Fail opening file.\n")
        return
    parsedInput = [(line.split()[0], int(line.split()[1]), getForce(line.split()[0])) for line in file]
    parsedInput.sort(key=functools.cmp_to_key(sortComparator))
    
    totalSum:int = 0
    for i in range(len(parsedInput)):
        #print(parsedInput[i], i + 1)
        totalSum += parsedInput[i][1] * (i + 1)
    print("The final value is: {}".format(totalSum))

if __name__ == "__main__":
    main()