# Advent of Code 2023
# Solution of day 8 puzzle part 2
#
# Author Alonso Sayalero
from math import gcd

def main():
    try:
        file = open("./input.txt", "r").read().splitlines()
    except:
        print("Fail opening file.\n")
        return
    
    traduction = {"L": 0, "R": 1}

    counter = 0
    instructions = file[0]
    nodes = {}
    nextNode = []
    for i in range(2, len(file)):
        node, nextNodes = file[i].split("=")
        node = node.split()[0]
        if node[2] == "A":
            nextNode.append(node)
        nextNodes = (nextNodes.split()[0].split(",")[0].split("(")[1], nextNodes.split()[1].split(")")[0])
        nodes[node] = nextNodes
        
    cycles = []
    for current in nextNode:
        cycle = []
        currentInstructions = instructions
        stepCount = 0
        firstZ = None

        while True:
            while stepCount == 0 or current[2] != "Z":
                stepCount += 1
                current = nodes[current][traduction[currentInstructions[0]]]
                currentInstructions = currentInstructions[1:] + currentInstructions[0]
            
            cycle.append(stepCount)

            if firstZ is None:
                firstZ = current
                stepCount = 0
            elif firstZ == current:
                break
        cycles.append(cycle)

    nums = [cycle[0] for cycle in cycles]

    lcm = nums.pop()
    for num in nums:
        lcm = lcm * num // gcd(lcm, num)

    print("The final value is: {}".format(lcm))

if __name__ == "__main__":
    main()