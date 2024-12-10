def load_input():
    with open("c:/Users/lucam/OneDrive/Desktop/advent_of_code/adventofcode/2024/tor_10/input.txt", "r") as f:
        return f.read().strip()
    
def part1(input):
    trails = []
    start_points = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    lines = input.split("\n")

    for i, line in enumerate(lines):
        digits = []
        for j, digit in enumerate(line):
            digits.append(int(digit))
            if int(digit) == 0:
                start_points.append((i, j))

        trails.append(digits)

    total_score = 0
    for start in start_points:
        queue = [start]
        reachable_endpoints = set()

        while queue:
            x, y = queue.pop(0)
            current_height = trails[x][y]

            for dx, dy in directions:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < len(trails) and 0 <= y1 < len(trails[0]): # prüef ob innerhalb trails
                    if trails[x1][y1] == current_height + 1: # nur wenns + 1 isch (chöntemer au prüefe ob visited isch (denn duet mer nöd unnötig viel glich witersueche))
                        queue.append((x1, y1))
                        if trails[x1][y1] == 9:
                            reachable_endpoints.add((x1, y1))

        score = len(reachable_endpoints)

        total_score += score
    
    return total_score


def part2(input):
    trails = []
    start_points = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    lines = input.split("\n")

    for i, line in enumerate(lines):
        digits = []
        for j, digit in enumerate(line):
            digits.append(int(digit))
            if int(digit) == 0:
                start_points.append((i, j))

        trails.append(digits)

    total_rating = 0
    for start in start_points:
        stack = [(start, [])] 
        visited_paths = set()

        while stack:
            (x, y), path = stack.pop() # miteme stack glöst: Speicheret immer die höchst trail pos und pfad det ane (vo jedem punkt denn i alli richtige etc.)
            current_height = trails[x][y]
            new_path = path + [(x, y)]

            if trails[x][y] == 9:
                visited_paths.add(tuple(new_path))
                continue

            for dx, dy in directions:
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < len(trails) and 0 <= y1 < len(trails[0]):
                    if trails[x1][y1] == current_height + 1:
                        stack.append(((x1, y1), new_path))

        total_rating += len(visited_paths)
    
    return total_rating


def main():
    input = load_input()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()