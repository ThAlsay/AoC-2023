# Advent of Code 2023
# Solution of day 9 puzzle part 1
#
# Author Alonso Sayalero

def extrapolate(array):
    if all(x == 0 for x in array):
        return 0
    
    deltas = [y - x for x, y in zip(array, array[1:])]
    difference = extrapolate(deltas)
    return array[-1] + difference

def main():
    try:
        file = open("./input.txt", "r").read().splitlines()
    except:
        print("Fail opening file.\n")
        return
    
    totalSum:int = 0
    for line in file:
        line = list(map(int, line.split()))
        totalSum += extrapolate(line)
            
    print("The final value is: {}".format(totalSum))

if __name__ == "__main__":
    main()