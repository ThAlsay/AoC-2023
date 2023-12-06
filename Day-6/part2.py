# Advent of Code 2023
# Solution of day 6 puzzle part 2
#
# Author Alonso Sayalero


def main():
    try:
        file = open("./input.txt", "r").read().splitlines()
    except:
        print("Fail opening file.\n")
        return
    
    time = int("".join(file[0].split()[1:]))
    distance = int("".join(file[1].split()[1:]))
    counter = 0
    for j in range(time + 1):
        if j * (time - j) > distance:
            break
        counter += 1

    print("The final value is: {}".format(time - 2 * counter + 1))

if __name__ == "__main__":
    main()