# Advent of Code 2023
# Solution of day 5 puzzle part 1
#
# Author Alonso Sayalero

def transformSeedList(seedArray: list[int], transformArray: list[list[int]]):
    for i in range(len(seedArray)):
        aux = seedArray[i]
        for j in range(len(transformArray)):
            if seedArray[i] >= transformArray[j][0] and seedArray[i] < transformArray[j][0] + transformArray[j][2]:
                aux = (seedArray[i] - transformArray[j][0]) + transformArray[j][1]
        seedArray[i] = aux

def extractList(file: list[str], counter: int):
    auxList = []
    while counter != len(file):
        if file[counter] == '':
            break
        destination, origin, rang = file[counter].split()
        auxList.append([int(origin), int(destination), int(rang)])
        counter += 1
    return auxList, counter

def main():
    try:
        file = open("./input.txt", "r").read().splitlines()
    except:
        print("Fail opening file.\n")
        return
    
    minLocation:int = 2147483647
    seeds = list(map(lambda i: int(i), file[0].split()[1:]))
    counter = 3

    while counter < len(file):
        transformList, counter = extractList(file, counter)
        transformSeedList(seeds, transformList)
        counter += 2
    
    for i in seeds:
        if i < minLocation:
            minLocation = i

    print("The final value is: {}".format(minLocation))

if __name__ == "__main__":
    main()