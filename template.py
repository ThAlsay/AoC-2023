# Advent of Code 2023
# Solution of day X puzzle part X
#
# Author Alonso Sayalero


def main():
    try:
        file = open("./input.txt", "r").read().splitlines()
    except:
        print("Fail opening file.\n")
        return
    
    totalSum:int = 0
    # file processing
    print("The final value is: {}".format(totalSum))

if __name__ == "__main__":
    main()