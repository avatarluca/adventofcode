def load_input():
    with open("c:/Users/lucam/OneDrive/Desktop/advent_of_code/adventofcode/tor_2/input.txt", "r") as f:
        return f.read().strip()

def part1(input):
    lines = input.split("\n")
    count = 0

    for line in lines:
        levels = line.split(" ")

        safe = True

        increasing = True
        decreasing = True

        for i in range(1, len(levels)):
            if int(levels[i]) > int(levels[i - 1]):
                decreasing = False
            elif int(levels[i]) < int(levels[i - 1]):
                increasing = False

        if increasing == False and decreasing == False:
            continue

        for i in range(1, len(levels)):
            if abs(int(levels[i]) - int(levels[i - 1])) > 3\
                or abs(int(levels[i]) - int(levels[i - 1])) < 1:
                
                safe = False

                break

        if safe:
            count += 1

    return count



def part2(input):
    lines = input.split("\n")
    count = 0

    for line in lines:
        levels = line.split(" ")

        safe = True

        increasing = True
        decreasing = True

        for i in range(1, len(levels)):
            if int(levels[i]) > int(levels[i - 1]):
                decreasing = False
            elif int(levels[i]) < int(levels[i - 1]):
                increasing = False

        if increasing == False and decreasing == False:
            safe = False

        if safe:
            for i in range(1, len(levels)):
                if abs(int(levels[i]) - int(levels[i - 1])) > 3\
                    or abs(int(levels[i]) - int(levels[i - 1])) < 1:
                    
                    safe = False

                    break

        if safe:
            count += 1
        else: 
            for num in range(0, len(levels)):
                new_levels = levels.copy()
                new_levels.pop(num)

                safe = True

                increasing = True
                decreasing = True

                for i in range(1, len(new_levels)):
                    if int(new_levels[i]) > int(new_levels[i - 1]):
                        decreasing = False
                    elif int(new_levels[i]) < int(new_levels[i - 1]):
                        increasing = False

                if increasing == False and decreasing == False:
                    safe = False

                if safe:
                    for i in range(1, len(new_levels)):
                        if abs(int(new_levels[i]) - int(new_levels[i - 1])) > 3\
                            or abs(int(new_levels[i]) - int(new_levels[i - 1])) < 1:
                            
                            safe = False

                            break
                        
                if safe:
                    count += 1
                    break


    return count

def main():
    input = load_input()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()