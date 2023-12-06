# Advent of Code 2023
# Solution of day 5 puzzle part 2
#
# Author Alonso Sayalero

def main():
    try:
        inputs, *blocks = open("./input.txt", "r").read().split("\n\n")
    except:
        print("Fail opening file.\n")
        return
    
    inputs = list(map(int, inputs.split(":")[1].split()))

    seeds = []
    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        while len(seeds) > 0:
            start, end = seeds.pop()
            for destination, origin, jump in ranges:
                overlapStart = max(start, origin)
                overlapEnd = min(end, origin + jump)
                if overlapStart < overlapEnd:
                    new.append((overlapStart - origin + destination, overlapEnd - origin + destination))
                    if overlapStart > start:
                        seeds.append((start, overlapStart))
                    if end > overlapEnd:
                        seeds.append((overlapEnd, end))
                    break
            else:
                new.append((start, end))
        seeds = new

    print(min(seeds)[0])

if __name__ == "__main__":
    main()