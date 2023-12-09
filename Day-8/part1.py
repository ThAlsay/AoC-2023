# Advent of Code 2023
# Solution of day 8 puzzle part 1
#
# Author Alonso Sayalero


def main():
    try:
        file = open("./input.txt", "r").read().splitlines()
    except:
        print("Fail opening file.\n")
        return
    
    traduction = {"L": 0, "R": 1}

    counter = 0
    index = 0
    instructions = file[0]
    nodes = {}
    nextNode = "AAA"
    for i in range(2, len(file)):
        node, nextNodes = file[i].split("=")
        node = node.split()[0]
        nextNodes = (nextNodes.split()[0].split(",")[0].split("(")[1], nextNodes.split()[1].split(")")[0])
        nodes[node] = nextNodes
    
    while True:
        if index == len(instructions):
            index = 0
        
        nextNode = nodes[nextNode][traduction[instructions[index]]]

        counter += 1
        if nextNode == "ZZZ":
            break
        index += 1

    print("The final value is: {}".format(counter))

if __name__ == "__main__":
    main()