def load_input():
    with open("c:/Users/lucam/OneDrive/Desktop/advent_of_code/adventofcode/2024/tor_14/input.txt", "r") as f:
        return f.read().strip()

def part1(input):
    width = 101
    height = 103
    seconds = 100

    lines = input.split("\n")
    
    plan = [[[] for _ in range(width)] for _ in range(height)]

    for line in lines:
        parts = line.split(" ")
        pos = parts[0].split("=")[1].split(",")
        vel = parts[1].split("=")[1].split(",")
       
        x = int(pos[0])
        y = int(pos[1])
        vx = int(vel[0])
        vy = int(vel[1])

        plan[y][x].append((vx, vy))
            
    for second in range(seconds):
        new_plan = [[[] for _ in range(width)] for _ in range(height)]
        for i in range(len(plan)):
            for j in range(len(plan[i])):
                while plan[i][j]:
                    vx, vy = plan[i][j].pop()
                    x = (j + vx) % width
                    y = (i + vy) % height
                    new_plan[y][x].append((vx, vy))
        plan = new_plan

    """for i in range(height):
        print("".join(["#" if len(plan[i][j]) > 0 else "." for j in range(width)]))"""

    quadrants = [0, 0, 0, 0]
    for i in range(height):
        for j in range(width):
            if len(plan[i][j]) > 0 and i != height // 2 and j != width // 2:
                if i < height // 2 and j < width // 2:
                    quadrants[0] += len(plan[i][j])
                elif i < height // 2 and j > width // 2:
                    quadrants[1] += len(plan[i][j])
                elif i > height // 2 and j < width // 2:
                    quadrants[2] += len(plan[i][j])
                else:
                    quadrants[3] += len(plan[i][j])

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def part2(input):
    width = 101
    height = 103

    lines = input.split("\n")
    
    plan = [[[] for _ in range(width)] for _ in range(height)]

    for line in lines:
        parts = line.split(" ")
        pos = parts[0].split("=")[1].split(",")
        vel = parts[1].split("=")[1].split(",")
       
        x = int(pos[0])
        y = int(pos[1])
        vx = int(vel[0])
        vy = int(vel[1])

        plan[y % height][x % width].append((vx, vy))
            
    # Idee: Wenn viel Roboter zäme sind, isch sicher es easteregg
    # Entweder (so wien ichs da gmacht han) chammer das mache idem mer luegt da so wenig wie möglich Päärli bildet hend (bzw. en robot_together counter)
    # Oder mer chan das au ander ume mache: Wenns es Päärli git mit mega viel Roboter zäme, denn isch dwahrschinlichkeit höher für es easteregg
        
    for second in range(1, 10**6):
        #print(second)

        new_plan = [[[] for _ in range(width)] for _ in range(height)]
        for i in range(len(plan)):
            for j in range(len(plan[i])):
                while plan[i][j]:
                    vx, vy = plan[i][j].pop()
                    x = (j + vx) % width
                    y = (i + vy) % height
                    new_plan[y][x].append((vx, vy))
        plan = new_plan

        robots_together = 0
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(height):
            for j in range(width):
                if len(plan[i][j]) > 0 and (i, j) not in visited:
                    robots_together += 1
                    stack = [(i, j)]

                    while stack:
                        ci, cj = stack.pop()
                        if (ci, cj) not in visited:
                            visited.add((ci, cj))

                            for di, dj in directions:
                                ni, nj = (ci + di) % height, (cj + dj) % width
                                if len(plan[ni][nj]) > 0 and (ni, nj) not in visited:
                                    stack.append((ni, nj))

        # robots together muess bim easteregg chliner si als sust wills ja eis grosses tannebaum päärli git
        # es staht "most of the robots" und nöd alli (drum nöd robots_together == 1) => Isch en bug gsi lol
        if robots_together <= 150: 
            """for i in range(height):
                print("".join(["#" if len(plan[i][j]) > 0 else "." for j in range(width)]))"""
            return second
        
        # Als erwiterig chamer evtl. eifach no en input handling mache zum witer loope wenn doch kei easteregg gfunde worde isch

    return -1

def main():
    input = load_input()

    print(part1(input))
    print(part2(input))


if __name__ == "__main__":
    main()
