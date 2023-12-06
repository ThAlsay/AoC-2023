# Advent of Code 2023
# Solution of day 6 puzzle part 1
#
# Author Alonso Sayalero


def main():
    try:
        file = open("./input.txt", "r").read().splitlines()
    except:
        print("Fail opening file.\n")
        return
    
    totalMult:int = 1
    time = list(map(int, file[0].split()[1:]))
    distance = list(map(int, file[1].split()[1:]))
    for i in range(len(time)):
        counter = 0
        for j in range(time[i] + 1):
            if j * (time[i] - j) > distance[i]:
                break
            counter += 1
        totalMult *= time[i] - 2 * counter + 1

    print("The final value is: {}".format(totalMult))

if __name__ == "__main__":
    main()