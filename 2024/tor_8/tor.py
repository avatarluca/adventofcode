def load_input():
    with open("c:/Users/lucam/OneDrive/Desktop/advent_of_code/adventofcode/2024/tor_8/input.txt", "r") as f:
        return f.read().strip()


def part1(input):
    antenna_maps = {}
    lines = input.split("\n")

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != ".":
                if char not in antenna_maps:
                    antenna_maps[char] = []
                antenna_maps[char].append((j, i))
   
    unique_antinodes = set()
    for char, positions in antenna_maps.items():
        for i, (x1, y1) in enumerate(positions):
            for x2, y2 in positions[i + 1:]: # für alli witeri paar (so gits kein unnötige doppeltcheck)
                dx, dy = x2 - x1, y2 - y1

                # Idee: Antinodes hend automatisch scho doppelti entfernig zude andere antenne wenn mer (dx, dy) und (-dx, -dy) hinzuefüegt
                x3, y3 = x2 + dx, y2 + dy
                x4, y4 = x1 - dx, y1 - dy

                if 0 <= x3 < len(lines[0]) and 0 <= y3 < len(lines):
                    unique_antinodes.add((x3, y3))
                if 0 <= x4 < len(lines[0]) and 0 <= y4 < len(lines):
                    unique_antinodes.add((x4, y4))

    return len(unique_antinodes)


def part2(input):
    antenna_maps = {}
    lines = input.split("\n")

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != ".":
                if char not in antenna_maps:
                    antenna_maps[char] = []
                antenna_maps[char].append((j, i))
   
    unique_antinodes = set()
    for char, positions in antenna_maps.items():
        for i, (x1, y1) in enumerate(positions):
            for x2, y2 in positions[i + 1:]: # für alli witeri paar (so gits kein unnötige doppeltcheck)
                dx, dy = x2 - x1, y2 - y1

                for y, line in enumerate(lines): 
                    for x, char in enumerate(line):
                        if (x - x1) * dy == (y - y1) * dx: # verglicht dstigig
                           unique_antinodes.add((x, y))
    
    return len(unique_antinodes)

def main():
    input = load_input()

    print(part1(input))
    print(part2(input))

if __name__ == "__main__":
    main()