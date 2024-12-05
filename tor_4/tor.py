def load_input():
    with open("c:/Users/lucam/OneDrive/Desktop/advent_of_code/adventofcode/tor_4/input.txt", "r") as f:
        return f.read().strip()

def part1(input):
    count = 0

    # horizontal
    for line in input.split("\n"):
        for i in range(len(line) - 3):
            if line[i:i+3] == "XMAS":
                count += 1
            elif line[i:i+3] == "SAMX":
                count += 1

    # vertikale   
    for i in range(len(input.split("\n")) - 3):
        for j in range(len(input.split("\n")[i])):
            if input.split("\n")[i][j] == "X" and input.split("\n")[i+1][j] == "M" and input.split("\n")[i+2][j] == "A" and input.split("\n")[i+3][j] == "S":
                count += 1
            elif input.split("\n")[i][j] == "S" and input.split("\n")[i+1][j] == "A" and input.split("\n")[i+2][j] == "M" and input.split("\n")[i+3][j] == "X":
                count += 1
    
    # diagonal links rechts
    for i in range(len(input.split("\n")) - 3):
        for j in range(len(input.split("\n")[i]) - 3):
            if input.split("\n")[i][j] == "X" and input.split("\n")[i+1][j+1] == "M" and input.split("\n")[i+2][j+2] == "A" and input.split("\n")[i+3][j+3] == "S":
                count += 1
            elif input.split("\n")[i][j] == "S" and input.split("\n")[i+1][j+1] == "A" and input.split("\n")[i+2][j+2] == "M" and input.split("\n")[i+3][j+3] == "X":
                count += 1
    
    # diagonal rechts links
    for i in range(len(input.split("\n")) - 3):
        for j in range(3, len(input.split("\n")[i])): # fangt bi 3 a, will chliner nöd möglich
            if input.split("\n")[i][j] == "X" and input.split("\n")[i+1][j-1] == "M" and input.split("\n")[i+2][j-2] == "A" and input.split("\n")[i+3][j-3] == "S":
                count += 1
            elif input.split("\n")[i][j] == "S" and input.split("\n")[i+1][j-1] == "A" and input.split("\n")[i+2][j-2] == "M" and input.split("\n")[i+3][j-3] == "X":
                count += 1

    # TODO: Optimierig wer wenn mehr wenn bspw. XMAS gfunde wird, dass er denn die loops jewils au um 4 verschiebt

    return count


def part2(input):
    count = 0
    for i in range(len(input.split("\n")) - 2): 
        for j in range(len(input.split("\n")[i]) - 2): 
            if input.split("\n")[i][j] == "M" and input.split("\n")[i+1][j+1] == "A" and input.split("\n")[i+2][j+2] == "S":
                if input.split("\n")[i][j+2] == "M" and input.split("\n")[i+1][j+1] == "A" and input.split("\n")[i+2][j] == "S":
                    count += 1
                elif input.split("\n")[i][j+2] == "S" and input.split("\n")[i+1][j+1] == "A" and input.split("\n")[i+2][j] == "M":
                    count += 1
            elif input.split("\n")[i][j] == "S" and input.split("\n")[i+1][j+1] == "A" and input.split("\n")[i+2][j+2] == "M":
                if input.split("\n")[i][j+2] == "M" and input.split("\n")[i+1][j+1] == "A" and input.split("\n")[i+2][j] == "S":
                    count += 1
                elif input.split("\n")[i][j+2] == "S" and input.split("\n")[i+1][j+1] == "A" and input.split("\n")[i+2][j] == "M":
                    count += 1
    
    return count


def main():
    input = load_input()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()